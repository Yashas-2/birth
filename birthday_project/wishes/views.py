from django.shortcuts import render

def home(request):
    return render(request, 'wishes/index.html')
