# Generated by Django 4.2 on 2024-02-14 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Factory',
        ),
    ]
