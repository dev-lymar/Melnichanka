import json
import os
from typing import Any

from django.core.cache import cache
from django.http import FileResponse
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from makedoc.services import Documents
from .serializers import (
    DataDocSerializer,
    DocumentsSimpleSerializer,
    FileNameSerializer,
    EmailInputSerializer,
)
from .tasks import send_email_with_attachment


class CreateDocsAPIView(APIView):
    """
    Responsible for creating documents based on data from the cache.
    """

    serializer_class = DocumentsSimpleSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cache_key = f"validated_data_{request.user.id}"
        validated_data = cache.get(cache_key)

        if validated_data is None:
            return Response(
                {"error": "No data found in cache"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validated_data = json.loads(validated_data)
        except json.JSONDecodeError:
            return Response({"error": "Invalid data in cache"}, status=status.HTTP_400_BAD_REQUEST)

        docs = Documents(validated_data)
        docs.update_documents()
        if docs.auto:
            docs.form_auto_document(request)
        if docs.rw:
            docs.form_rw_document(request)
        if docs.service_note:
            docs.form_service_note(request)
        if docs.transport_sheet:
            docs.form_transport_sheet(request)

        cache_key = f"last_created_file_user:{request.user.id}"
        cache.set(cache_key, docs.archive_name, 300)

        return Response({"message": "Documents saved"}, status=status.HTTP_200_OK)


class DownloadDocAPIView(APIView):
    """
    To download a file:

    - No parameters: get the last created file.

    - With the parameter {"file_name": "name your file"} - load a specific file from the list.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = FileNameSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": "Incorrect file name"}, status=status.HTTP_404_NOT_FOUND)

        file_name = serializer.validated_data.get("file_name")

        if not file_name:
            cache_key = f"last_created_file_user:{request.user.id}"
            file_name = cache.get(cache_key)

            if not file_name:
                return Response({"error": "No file found"}, status=status.HTTP_404_NOT_FOUND)

        file_path = os.path.join("makedoc", "tempdoc", str(request.user.id), file_name)

        if not os.path.exists(file_path):
            return Response({"error": "File path not found!"}, status=status.HTTP_404_NOT_FOUND)

        response = FileResponse(open(file_path, "rb"))
        response["Content-Disposition"] = f'attachment; filename="{os.path.basename(file_name)}"'
        response["message"] = "File successfully downloaded"
        response.status_code = status.HTTP_200_OK

        return response


class DataDocAPIView(generics.GenericAPIView[Any]):
    """
    Responsible for receiving data, validating it and storing it in cache.
    """

    serializer_class = DataDocSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        cache_key = f"validated_data_{request.user.id}"
        cache.set(cache_key, json.dumps(validated_data), 120)

        return Response({"Success": True}, status=status.HTTP_200_OK)


class SendArchiveAPIView(APIView):
    """
    API endpoint to send an email with an attachment.
    """

    def post(self, request, *args, **kwargs):
        serializer = EmailInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get("email")
        full_name = request.user.full_name

        cache_key = f"last_created_file_user:{request.user.id}"
        file_name = cache.get(cache_key)

        if not file_name:
            return Response({"error": "No file found in cache"}, status=status.HTTP_404_NOT_FOUND)

        file_path = os.path.join("makedoc", "tempdoc", str(request.user.id), file_name)

        if not os.path.exists(file_path):
            return Response({"error": "File path not found!"}, status=status.HTTP_404_NOT_FOUND)

        send_email_with_attachment.delay(email, file_path, full_name=full_name)

        return Response({"message": "Email will be sent shortly."}, status=status.HTTP_200_OK)
