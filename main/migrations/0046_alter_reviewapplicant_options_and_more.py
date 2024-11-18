# Generated by Django 5.0.1 on 2024-07-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_reviewapplicant_alter_approvedapplicant_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewapplicant',
            options={'verbose_name': ' Review Applicant'},
        ),
        migrations.AddField(
            model_name='uploadapplicant',
            name='klasifikasiSKA',
            field=models.CharField(blank=True, choices=[('', '--Silahkan Pilih--'), ('Muda', 'Muda'), ('Madya', 'Madya'), ('Utama', 'Utama')], max_length=5),
        ),
        migrations.AddField(
            model_name='uploadapplicant',
            name='subklasifikasiSKA',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='uploadapplicant',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Reject', 'Reject'), ('Approve', 'Approve'), ('On Review', 'On Review')], default='Pending', max_length=20, verbose_name='Status'),
        ),
    ]