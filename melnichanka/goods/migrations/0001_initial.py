# Generated by Django 4.2 on 2024-02-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flour_name', models.CharField(choices=[('экстра', 'Мука пшеничная хлебопекарная сорт экстра'), ('цз', 'Мука цельнозерновая'), ('вс', 'Мука пшеничная хлебопекарная высший сорт'), ('1с', 'Мука пшеничная хлебопекарная первый сорт'), ('2с', 'Мука пшеничная хлебопекарная второй сорт'), ('55', 'Мука пшеничная общего назначения тип М55-23'), ('75', 'Мука пшеничная общего назначения тип М75-23'), ('ржо', 'Мука ржаная обдирная'), ('ржс', 'Мука ржаная сеяная'), ('ман', 'Крупа манная марка М')], max_length=255, verbose_name='Сорт муки')),
                ('unit_weight', models.PositiveIntegerField(verbose_name='Вес единицы')),
                ('group_quantity', models.PositiveIntegerField(verbose_name='Количество штук в упаковке')),
                ('pallet_weight', models.PositiveIntegerField(verbose_name='Вес на паллете')),
                ('brand', models.CharField(choices=[('na', ''), ('фшэ', 'Французская штучка'), ('фшхп', 'Французская штучка для хлебопечки'), ('бн', 'Бело-Нежная'), ('сл', 'Славна'), ('со', 'Старооскольская'), ('кур', 'Курская'), ('акц', 'Акция')], max_length=255, verbose_name='Брэнд')),
                ('price', models.FloatField()),
            ],
        ),
    ]
