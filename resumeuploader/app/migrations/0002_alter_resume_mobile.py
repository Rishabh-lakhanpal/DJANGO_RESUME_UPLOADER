# Generated by Django 4.1.4 on 2022-12-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
    ]