# Generated by Django 3.0.3 on 2020-02-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200213_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='price_large',
            field=models.FloatField(null=True),
        ),
    ]