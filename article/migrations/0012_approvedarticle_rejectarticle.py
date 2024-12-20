# Generated by Django 5.0.1 on 2024-08-05 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_article_artstatus_alter_article_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedArticle',
            fields=[
            ],
            options={
                'verbose_name': '  Approve Article',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('article.article',),
        ),
        migrations.CreateModel(
            name='RejectArticle',
            fields=[
            ],
            options={
                'verbose_name': '  Reject Article',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('article.article',),
        ),
    ]
