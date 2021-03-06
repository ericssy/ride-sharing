# Generated by Django 2.2.5 on 2019-11-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rideshare_app', '0007_auto_20191108_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('venmo', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('car_make', models.CharField(blank=True, max_length=30, null=True)),
                ('car_model', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
