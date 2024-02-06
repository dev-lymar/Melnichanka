# Generated by Django 4.2 on 2024-02-06 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0008_alter_factory_full_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RailwayStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(choices=[('Курск', 'Рышково'), ('Оскол', 'Старый Оскол'), ('Волгоград', 'Карповская')], max_length=255, verbose_name='Станция')),
                ('station_id', models.PositiveIntegerField()),
                ('station_branch', models.CharField(choices=[('ОЖД', 'Октябрьская железная дорога'), ('КаЖД', 'Калининградская железная дорога'), ('МЖД', 'Московская железная дорога'), ('ГЖД', 'Горьковская железная дорога'), ('СеЖД', 'Северная железная дорога'), ('СКЖД', 'Северо-Кавказская железная дорога'), ('ЮВЖД', 'Юго-Восточная железная дорога'), ('ПЖД', 'Приволжская железная дорога'), ('КуЖД', 'Куйбышевская железная дорога'), ('СвЖД', 'Свердловская железная дорога'), ('ЮУЖД', 'Южно-Уральская железная дорога'), ('ЗСЖД', 'Западно-Сибирская железная дорога'), ('КЖД', 'Красноярская железная дорога'), ('ВСЖД', 'Восточно-Сибирская железная дорога'), ('ЗЖД', 'Забайкальская железная дорога'), ('ДВЖД', 'Дальневосточная железная дорога')], max_length=255)),
            ],
            options={
                'verbose_name': 'Ж/д станция',
                'verbose_name_plural': 'Ж/д станции',
                'ordering': ['station_name'],
            },
        ),
        migrations.RemoveField(
            model_name='logisticsrailwaystations',
            name='departure_station_branch',
        ),
        migrations.RemoveField(
            model_name='logisticsrailwaystations',
            name='departure_station_id',
        ),
        migrations.RemoveField(
            model_name='logisticsrailwaystations',
            name='destination_station_branch',
        ),
        migrations.RemoveField(
            model_name='logisticsrailwaystations',
            name='destination_station_id',
        ),
        migrations.AlterField(
            model_name='logisticsrailwaystations',
            name='departure_station_name',
            field=models.ForeignKey(db_column='departure_station_name', on_delete=django.db.models.deletion.CASCADE, related_name='departure_station_name', to='logistics.railwaystations'),
        ),
        migrations.AlterField(
            model_name='logisticsrailwaystations',
            name='destination_station_name',
            field=models.ForeignKey(db_column='destination_station_name', on_delete=django.db.models.deletion.CASCADE, related_name='destination_station_name', to='logistics.railwaystations'),
        ),
    ]
