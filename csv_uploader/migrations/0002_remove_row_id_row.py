# Generated by Django 3.2 on 2021-04-24 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_uploader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='row',
            name='id_row',
        ),
    ]
