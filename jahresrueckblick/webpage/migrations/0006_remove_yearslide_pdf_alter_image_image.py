# Generated by Django 4.1.7 on 2023-03-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_yearslide_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yearslide',
            name='pdf',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text='Bitte lade ein Bild hoch.', upload_to='media/images/'),
        ),
    ]
