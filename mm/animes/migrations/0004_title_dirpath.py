# Generated by Django 2.1.2 on 2019-01-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_auto_20190103_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='dirPath',
            field=models.FilePathField(null=True),
        ),
    ]
