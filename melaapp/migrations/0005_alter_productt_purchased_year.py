# Generated by Django 3.2.12 on 2022-03-19 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melaapp', '0004_auto_20220319_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productt',
            name='purchased_year',
            field=models.IntegerField(),
        ),
    ]
