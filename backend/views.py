from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def article(request):
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles': articles})