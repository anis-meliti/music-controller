# Generated by Django 3.2.9 on 2022-06-18 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='cotes_to_skip',
            new_name='votes_to_skip',
        ),
    ]
