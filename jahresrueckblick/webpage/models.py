from django.db import models

# Create a year model
class YearSlide(models.Model):
    year = models.IntegerField(help_text="Bitte gib das Jahr an, für das du diesen Slide erstellen möchtest. Nach diesem Wert wird sortiert.")
    title = models.CharField(max_length=800, blank=True, help_text="Du kannst einen abweichenden Titel für die Slide angeben. Ist dieses Feld leer, wird das Jahr angezeigt.")
    slogan = models.TextField(blank=True, help_text="Du kannst ein Motto oder ein Thema für das Jahr angeben. Ist dieses Feld leer, wird nichts angezeigt.")
    document = models.FileField(upload_to='media/pdfs/', blank=True, null=True, help_text="Du kannst eine PDF-Datei hochladen, die zu diesem Jahr gehört. Ist dieses Feld leer, wird nichts angezeigt.")
    document_image = models.ImageField(upload_to='media/images/', blank=True, null=True, help_text="Du kannst ein Vorschaubild hochladen, das zu diesem Dokument gehört. Ist dieses Feld leer, wird nichts angezeigt.")

    def name(self):
        if self.title:
            return self.title
        else:
            return self.year

    def __str__(self):
        return str(self.name()) + " - " + str(self.slogan)
    
# Create a Image model
class Highlight(models.Model):
    year = models.ForeignKey(YearSlide, on_delete=models.CASCADE)
    title = models.CharField(max_length=800, help_text="Bitte gib einen Titel für das Bild an.")
    image = models.ImageField(upload_to='media/images/', help_text="Bitte lade ein Bild hoch.")
    description = models.TextField(help_text="Bitte gib eine Beschreibung für das Event an.")
    date = models.DateField(help_text="Bitte gib das Datum für das Event an.")
    location = models.CharField(max_length=800, help_text="Bitte gib den Ort für das Event an.")
    
    def __str__(self):
        return self.title + " - " + str(self.year.year)
# Create a position model combining year and person
class Position(models.Model):
    year = models.ForeignKey(YearSlide, on_delete=models.CASCADE)
    person = models.CharField(max_length=800, help_text="Bitte gib den Namen der Person an.")
    position = models.CharField(max_length=800, help_text="Bitte gib die Position an, die die Person im Jahr innehatte.")
    chairman = models.BooleanField(default=False, help_text="Bitte gib an, ob die Person Vorsitzender war.")

    def __str__(self):
        return self.person + " - " + self.position + " - " + str(self.year.year)
    
# Create a hounour model
class Honour(models.Model):
    year = models.ForeignKey(YearSlide, on_delete=models.CASCADE)
    person = models.CharField(max_length=800, help_text="Bitte gib den Namen der Person an.")
    honour = models.CharField(max_length=800, help_text="Bitte gib die Auszeichnung an, die die Person im Jahr erhalten hat.")
    
    def __str__(self):
        return self.person + " - " + self.honour + " - " + str(self.year.year)