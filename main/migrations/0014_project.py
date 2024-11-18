# Generated by Django 5.0.1 on 2024-05-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_map_map_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id_pekerjaan', models.AutoField(primary_key=True, serialize=False)),
                ('namaPekerjaan', models.CharField(max_length=200)),
                ('latCoor', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longCoor', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
