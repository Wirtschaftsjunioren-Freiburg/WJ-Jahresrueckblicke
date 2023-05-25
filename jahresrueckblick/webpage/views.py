from django.shortcuts import render
from .models import *

# render index file
def index(request):
    # Get all year slides
    years = YearSlide.objects.all().order_by('-year')
    return render(request, 'index.html', {'years': years})
