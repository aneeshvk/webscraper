# Generated by Django 4.0.5 on 2022-06-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='newproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectdetails', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('funddetails', models.CharField(max_length=200)),
            ],
        ),
    ]