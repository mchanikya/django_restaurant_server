# Generated by Django 3.0.3 on 2020-02-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200213_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='short_name',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
