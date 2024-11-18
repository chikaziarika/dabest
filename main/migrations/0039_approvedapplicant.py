# Generated by Django 5.0.1 on 2024-07-05 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_uploadapplicant_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.uploadapplicant')),
            ],
            options={
                'ordering': ['approved_date'],
            },
        ),
    ]