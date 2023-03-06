from django.contrib import admin

# Add all models to django admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class YearSlideResource(resources.ModelResource):
    class Meta:
        model = YearSlide

class EventResource(resources.ModelResource):
    class Meta:
        model = Event

class ImageResource(resources.ModelResource):
    class Meta:
        model = Image

class PositionResource(resources.ModelResource): 
    class Meta:
        model = Position

class HonourResource(resources.ModelResource):     
    class Meta:
        model = Honour


admin.site.register(YearSlide,ImportExportModelAdmin)
admin.site.register(Event,ImportExportModelAdmin)
admin.site.register(Image,ImportExportModelAdmin)
admin.site.register(Position,ImportExportModelAdmin)
admin.site.register(Honour,ImportExportModelAdmin)