# Generated by Django 5.0.1 on 2024-06-19 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_departementlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='department',
            field=models.ForeignKey(blank=True, default='Departement', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.departementlist'),
        ),
        migrations.AlterField(
            model_name='departementlist',
            name='jobList',
            field=models.CharField(max_length=200, verbose_name='DEPARTEMENT'),
        ),
    ]
