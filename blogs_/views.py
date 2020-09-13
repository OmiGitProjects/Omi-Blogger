#TODO: Blog Management App
from django.shortcuts import render

# Rendering Homepage
def index(request):
    context = {}
    return render(request, 'blogs_/index.html', context)