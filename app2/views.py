from django.shortcuts import render

def home(request):
    return render(request, 'app2/base.html')
