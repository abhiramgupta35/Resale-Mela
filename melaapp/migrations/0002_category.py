# Generated by Django 3.2.12 on 2022-03-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
    ]