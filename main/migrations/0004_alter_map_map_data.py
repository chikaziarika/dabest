# Generated by Django 5.0.1 on 2024-04-26 03:15

import gdstorage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_map_map_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='map_data',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='1u7zkQowv07RSPBpBX4IlP3DXrZTFQyBg'),
        ),
    ]