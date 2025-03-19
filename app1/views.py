from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    authors = Author.objects.filter(popularity_score__gte=8, firstname__startswith='A').values_list('firstname', 'popularity_score')
    print(authors)
    return render(request, 'app1/base.html')