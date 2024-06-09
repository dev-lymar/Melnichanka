# Generated by Django 4.2 on 2024-06-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_alter_city_unique_together_alter_city_region_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное название предприятия')),
                ('short_name', models.CharField(max_length=100, verbose_name='Краткое название предприятия')),
                ('full_address', models.CharField(max_length=100, verbose_name='Адрес предприятия')),
                ('departure_city', models.CharField(max_length=100, verbose_name='Город отправления')),
                ('departure_station_branch', models.CharField(choices=[('ОЖД', 'Октябрьская ж/д'), ('КаЖД', 'Калининградская ж/д'), ('МЖД', 'Московская ж/д'), ('ГЖД', 'Горьковская ж/д'), ('СеЖД', 'Северная ж/д'), ('СКЖД', 'Северо-Кавказская ж/д'), ('ЮВЖД', 'Юго-Восточная ж/д'), ('ПЖД', 'Приволжская ж/д'), ('КуЖД', 'Куйбышевская ж/д'), ('СвЖД', 'Свердловская ж/д'), ('ЮУЖД', 'Южно-Уральская ж/д'), ('ЗСЖД', 'Западно-Сибирская ж/д'), ('КЖД', 'Красноярская ж/д'), ('ВСЖД', 'Восточно-Сибирская ж/д'), ('ЗЖД', 'Забайкальская ж/д'), ('ДВЖД', 'Дальневосточная ж/д')], max_length=100, verbose_name='Ветка ж/д стации')),
                ('departure_station_id', models.PositiveIntegerField(verbose_name='Код ж/д стации')),
                ('departure_station_name', models.CharField(max_length=100, verbose_name='Ж/Д станция')),
            ],
            options={
                'verbose_name': 'Предприятие',
                'verbose_name_plural': 'Предприятия',
                'ordering': ['-full_name'],
                'unique_together': {('full_name', 'short_name', 'full_address')},
            },
        ),
    ]
