# Generated by Django 5.0.1 on 2024-07-17 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_article_image_alter_issue_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=50, verbose_name='HEADER'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='headline',
            field=models.CharField(max_length=50, verbose_name='HEADER'),
        ),
        migrations.AlterField(
            model_name='mainarticle',
            name='bigTitle',
            field=models.CharField(max_length=10, verbose_name='BIG TITLE'),
        ),
    ]
