# Generated by Django 2.1.2 on 2019-01-01 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20190101_1356'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cast',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
