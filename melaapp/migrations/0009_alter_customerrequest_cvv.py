# Generated by Django 3.2.12 on 2022-03-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melaapp', '0008_customerrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='cvv',
            field=models.IntegerField(max_length=3),
        ),
    ]
