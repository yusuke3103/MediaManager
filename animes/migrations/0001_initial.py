# Generated by Django 2.1.2 on 2019-01-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('tid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('firstYear', models.CharField(max_length=4)),
                ('firstMonth', models.CharField(max_length=2)),
                ('firstEndYear', models.CharField(max_length=4, null=True)),
                ('firstEndMonth', models.CharField(max_length=2, null=True)),
                ('comment', models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]