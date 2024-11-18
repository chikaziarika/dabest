# Generated by Django 5.0.1 on 2024-06-19 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_career_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='department',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='department', to='main.departementlist', to_field='jobList'),
        ),
        migrations.AlterField(
            model_name='departementlist',
            name='jobList',
            field=models.CharField(max_length=200, unique=True, verbose_name='DEPARTEMENT'),
        ),
    ]
