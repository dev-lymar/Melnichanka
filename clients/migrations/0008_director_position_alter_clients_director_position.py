# Generated by Django 4.2 on 2024-03-25 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_alter_clients_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director_position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_position', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Должность директора',
                'verbose_name_plural': 'Должность директора',
            },
        ),
        migrations.AlterField(
            model_name='clients',
            name='director_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.director_position', verbose_name='Должность директора'),
        ),
    ]