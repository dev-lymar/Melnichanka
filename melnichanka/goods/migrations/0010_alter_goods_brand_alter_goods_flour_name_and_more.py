# Generated by Django 4.2 on 2024-02-28 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_alter_goods_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand_goods', to='goods.brand'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='flour_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flour_goods', to='goods.flour'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_goods', to='goods.package'),
        ),
    ]
