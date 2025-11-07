from django.shortcuts import render
from .models import Pet

# Create your views here.
def Home(request):
    pets = Pet.objects.all()
    render(request , 'home.html' , {'pets' : pets})