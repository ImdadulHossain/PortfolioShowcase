from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, 'ShowCase/index.html', context)

# Create your views here.
