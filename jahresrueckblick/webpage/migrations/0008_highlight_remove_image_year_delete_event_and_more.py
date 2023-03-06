# Generated by Django 4.1.7 on 2023-03-06 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_yearslide_document_yearslide_document_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Bitte gib einen Titel für das Bild an.', max_length=800)),
                ('image', models.ImageField(help_text='Bitte lade ein Bild hoch.', upload_to='media/images/')),
                ('description', models.TextField(help_text='Bitte gib eine Beschreibung für das Event an.')),
                ('date', models.DateField(help_text='Bitte gib das Datum für das Event an.')),
                ('location', models.CharField(help_text='Bitte gib den Ort für das Event an.', max_length=800)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.yearslide')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='year',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
