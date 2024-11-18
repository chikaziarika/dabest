# Generated by Django 5.0.1 on 2024-04-26 02:45

import gdstorage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('map_name', models.CharField(max_length=200)),
                ('map_data', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='maps/')),
            ],
        ),
    ]