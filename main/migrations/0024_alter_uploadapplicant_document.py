# Generated by Django 5.0.1 on 2024-06-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_inputapplicant_uploadapplicant_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadapplicant',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='files/%y'),
        ),
    ]