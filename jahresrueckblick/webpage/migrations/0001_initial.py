# Generated by Django 4.1.7 on 2023-03-06 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Bitte gib den Namen der Person an.', max_length=800)),
                ('company', models.CharField(help_text='Bitte gib den Namen des Arbeitgebers an.', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='YearSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(help_text='Bitte gib das Jahr an, für das du diesen Slide erstellen möchtest. Nach diesem Wert wird sortiert.')),
                ('title', models.CharField(help_text='Du kannst einen abweichenden Titel für die Slide angeben. Ist dieses Feld leer, wird das Jahr angezeigt.', max_length=800)),
                ('slogan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(help_text='Bitte gib die Position an, die die Person im Jahr innehatte.', max_length=800)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.person')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.yearslide')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Bitte gib einen Titel für das Bild an.', max_length=800)),
                ('image', models.ImageField(help_text='Bitte lade ein Bild hoch.', upload_to='images/')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.yearslide')),
            ],
        ),
        migrations.CreateModel(
            name='Honour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('honour', models.CharField(help_text='Bitte gib die Auszeichnung an, die die Person im Jahr erhalten hat.', max_length=800)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.person')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.yearslide')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Bitte gib einen Titel für das Event an.', max_length=800)),
                ('description', models.TextField(help_text='Bitte gib eine Beschreibung für das Event an.')),
                ('date', models.DateField(help_text='Bitte gib das Datum für das Event an.')),
                ('location', models.CharField(help_text='Bitte gib den Ort für das Event an.', max_length=800)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.yearslide')),
            ],
        ),
    ]
