# Generated by Django 4.0.5 on 2022-07-03 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_expenditure_expenditure_exp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenditure',
            old_name='exp',
            new_name='expenditure',
        ),
    ]
