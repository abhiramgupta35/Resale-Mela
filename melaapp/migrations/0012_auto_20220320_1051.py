# Generated by Django 3.2.12 on 2022-03-20 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('melaapp', '0011_customerrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequest',
            name='cvv',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melaapp.sellregister'),
        ),
    ]