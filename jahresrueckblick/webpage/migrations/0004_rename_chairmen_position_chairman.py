# Generated by Django 4.1.7 on 2023-03-06 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_position_chairmen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='chairmen',
            new_name='chairman',
        ),
    ]
