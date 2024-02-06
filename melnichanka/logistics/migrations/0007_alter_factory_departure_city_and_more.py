# Generated by Django 4.2 on 2024-02-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "logistics",
            "0006_alter_factory_options_alter_factory_departure_city_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="factory",
            name="departure_city",
            field=models.CharField(
                choices=[
                    ("Курск", "Курск"),
                    ("Оскол", "Старый Оскол"),
                    ("Волгоград", "Новый Рогачик"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="factory",
            name="departure_station_branch",
            field=models.CharField(
                choices=[
                    ("Курск", "Московская железная дорога"),
                    ("Оскол", "Юго-Восточная железная дорога"),
                    ("Волгоград", "Приволжская железная дорога"),
                ],
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="factory",
            name="departure_station_id",
            field=models.CharField(
                choices=[
                    ("Курск", "208108"),
                    ("Оскол", "438506"),
                    ("Волгоград", "615904"),
                ],
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="factory",
            name="full_address",
            field=models.CharField(
                choices=[
                    ("Курск", "305025, г. Курск, проезд Магистральный, 22Г "),
                    (
                        "Оскол",
                        "309506, Белгородская обл., г. Старый Оскол, ул. Первой Конной Армии",
                    ),
                    (
                        "Волгоград",
                        "403020, Волгоградская обл., р.п. Новый Рогачик, ул. Ленина, 75",
                    ),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="factory",
            name="full_name",
            field=models.CharField(
                choices=[
                    ("Курск", "АО Курский Комбинат Хлебопродуктов"),
                    ("Оскол", "АО Комбинат Хлебопродуктов Старооскольский"),
                    ("Волгоград", "АО Городищенский Комбинат Хлебопродуктов"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="factory",
            name="short_name",
            field=models.CharField(
                choices=[("Курск", "ККХП"), ("Оскол", "КХПС"), ("Волгоград", "ГКХП")],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="logisticsrailwaystations",
            name="departure_station_name",
            field=models.CharField(
                choices=[
                    ("Рышково", "АО Курский Комбинат Хлебопродуктов"),
                    ("Старый Оскол", "АО Комбинат Хлебопродуктов Старооскольский"),
                    ("Карповская", "АО Городищенский Комбинат Хлебопродуктов"),
                ],
                max_length=255,
                verbose_name="Комбинат грузоотправитель",
            ),
        ),
    ]
