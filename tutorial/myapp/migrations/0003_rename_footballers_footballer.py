# Generated by Django 5.0.7 on 2024-09-29 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_foot_footballers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Footballers',
            new_name='Footballer',
        ),
    ]
