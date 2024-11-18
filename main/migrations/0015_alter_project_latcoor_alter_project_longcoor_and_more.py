# Generated by Django 5.0.1 on 2024-05-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latCoor',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='LATITTUDE'),
        ),
        migrations.AlterField(
            model_name='project',
            name='longCoor',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='LONGITUDE'),
        ),
        migrations.AlterField(
            model_name='project',
            name='namaPekerjaan',
            field=models.CharField(max_length=200, verbose_name='NAMA PEKERJAAN'),
        ),
    ]