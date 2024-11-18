# Generated by Django 5.0.1 on 2024-06-11 03:44

import phone_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_inputapplicant_countrycode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputapplicant',
            name='Gender',
            field=models.CharField(choices=[('LAKI - LAKI', 'LAKI - LAKI'), ('PEREMPUAN', 'PEREMPUAN')], max_length=20, verbose_name='JENIS KELAMIN'),
        ),
        migrations.AlterField(
            model_name='inputapplicant',
            name='Nationality',
            field=models.CharField(max_length=20, verbose_name='WARGA NEGARA'),
        ),
        migrations.AlterField(
            model_name='inputapplicant',
            name='expectedSalary',
            field=models.IntegerField(verbose_name='SALARY'),
        ),
        migrations.AlterField(
            model_name='inputapplicant',
            name='grossSalary',
            field=models.IntegerField(verbose_name='GROSS SALARY'),
        ),
        migrations.AlterField(
            model_name='inputapplicant',
            name='jobPosition',
            field=models.CharField(blank=True, max_length=255, verbose_name='JOB APPLICANT FOR'),
        ),
        migrations.AlterField(
            model_name='inputapplicant',
            name='personalMobile',
            field=phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='NO. TELEPHONE'),
        ),
    ]
