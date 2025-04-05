from django.shortcuts import render,redirect

def home(request):
    return render(request, 'home.html')  # Render the home.html template

# Create your views here.
