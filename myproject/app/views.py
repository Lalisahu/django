from django.shortcuts import render,redirect

def home(request):
    return render(request, 'home.html')  # Render the home.html template
def Home(request):
    return render(request, 'Home.html')  # Render the Home.html template

# Create your views here.
