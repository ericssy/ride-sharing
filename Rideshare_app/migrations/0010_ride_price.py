# Generated by Django 2.2.5 on 2019-11-11 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rideshare_app', '0009_auto_20191109_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]