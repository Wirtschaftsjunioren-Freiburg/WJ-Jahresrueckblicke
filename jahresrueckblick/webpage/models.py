from django.db import models

# Create a year model
class YearSlide(models.Model):

    class Meta:
        verbose_name = "Jahresrückblick (Jahr)"
        verbose_name_plural = "Jahresrückblicke (Jahre)"

    year = models.IntegerField(verbose_name="Jahreszahl", help_text="Bitte gib das Jahr an, für das du diesen Slide erstellen möchtest. Nach diesem Wert wird sortiert.")
    title = models.CharField(verbose_name="Titel", max_length=800, blank=True, help_text="Du kannst einen abweichenden Titel für die Slide angeben. Ist dieses Feld leer, wird das Jahr angezeigt.")
    slogan = models.TextField(blank=True, verbose_name="Motto", help_text="Du kannst ein Motto oder ein Thema für das Jahr angeben. Ist dieses Feld leer, wird nichts angezeigt.")
    document = models.FileField(blank=True, null=True, verbose_name="Jahresrückblick (PDF)", help_text="Du kannst eine PDF-Datei hochladen, die zu diesem Jahr gehört. Ist dieses Feld leer, wird nichts angezeigt.")
    document_image = models.ImageField(blank=True, null=True, verbose_name="Jahresrückblick (Titelbild)", help_text="Du kannst ein Vorschaubild hochladen, das zu diesem Dokument gehört. Ist dieses Feld leer, wird nichts angezeigt.")

    def name(self):
        if self.title:
            return self.title
        else:
            return self.year

    def __str__(self):
        return str(self.name()) + " - " + str(self.slogan)
    
# Create a Highlight model
class Highlight(models.Model):

    class Meta:
        verbose_name = "Highlight"

    year = models.ForeignKey(YearSlide, on_delete=models.CASCADE, verbose_name="Jahresrückblick / Jahr")
    title = models.CharField(max_length=800, verbose_name="Titel", help_text="Bitte gib einen Titel für das Bild an.")
    image = models.ImageField(verbose_name="Foto / Bild", help_text="Bitte lade ein Bild hoch. Bevorzugt einzelen Bilder mit einem Motiv im Mittelpunkt.")
    description = models.TextField(verbose_name="Beschreibung / Text", help_text="Bitte gib eine Beschreibung für das Event an.")
    date = models.DateField(verbose_name="Veranstaltungsdatum", help_text="Bitte gib das Datum für das Event an.")
    location = models.CharField(max_length=800, verbose_name="Veranstaltungsort", help_text="Bitte gib den Ort für das Event an.")
    
    def __str__(self):
        return self.title + " - " + str(self.year.year)
    
# Create an Image model
class Image(models.Model):

    class Meta:
        verbose_name = "Einzelbild"
        verbose_name_plural = "Einzelbilder"

    year = models.ForeignKey(YearSlide, on_delete=models.CASCADE, verbose_name="Jahresrückblick / Jahr")
    image = models.ImageField(verbose_name="Foto / Bild", help_text="Bitte lade ein Bild hoch.")
    description = models.TextField(verbose_name="Beschreibung / Titel", help_text="Bitte gib eine Beschreibung an - zum Beispiel Anlass, Datum, Ort,...")
    
    def __str__(self):
        return self.description + " - " + str(self.year.year)
    
# Create a position model combining year and person
class Position(models.Model):

    class Meta:
        verbose_name = "Person / Rolle"
        verbose_name_plural = "Personen / Rollen"

    year = models.ForeignKey(YearSlide, on_delete=models.CASCADE, verbose_name="Jahresrückblick / Jahr")
    person = models.CharField(verbose_name="Name der Person", max_length=800, help_text="Bitte gib den Namen der Person an.")
    position = models.CharField(verbose_name="Position", max_length=800, help_text="Bitte gib die Position an, die die Person im Jahr innehatte.")
    chairman = models.BooleanField(verbose_name="Ist Vorsitzender?", default=False, help_text="Bitte gib an, ob die Person Vorsitzender war.")

    def __str__(self):
        return self.person + " - " + self.position + " - " + str(self.year.year)
    
# Create a hounour model
class Honour(models.Model):

    class Meta:
        verbose_name = "Ehrung"
        verbose_name_plural = "Ehrungen"

    year = models.ForeignKey(YearSlide, on_delete=models.CASCADE, verbose_name="Jahresrückblick / Jahr")
    person = models.CharField(verbose_name="Name der Person", max_length=800, help_text="Bitte gib den Namen der Person an.")
    honour = models.CharField(verbose_name="Name der Ehrung", max_length=800, help_text="Bitte gib die Auszeichnung an, die die Person im Jahr erhalten hat.")
    
    def __str__(self):
        return self.person + " - " + self.honour + " - " + str(self.year.year)