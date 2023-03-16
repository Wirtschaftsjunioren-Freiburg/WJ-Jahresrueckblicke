# Generated by Django 4.1.7 on 2023-03-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_rename_chairmen_position_chairman'),
    ]

    operations = [
        migrations.AddField(
            model_name='yearslide',
            name='pdf',
            field=models.FileField(blank=True, help_text='Du kannst eine PDF-Datei hochladen, die zu diesem Jahr gehört. Ist dieses Feld leer, wird nichts angezeigt.', upload_to='pdfs/'),
        ),
    ]