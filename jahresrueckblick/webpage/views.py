from django.shortcuts import render

# render index file
def index(request):
    return render(request, 'index.html')