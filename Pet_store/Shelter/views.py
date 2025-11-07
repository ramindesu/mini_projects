from django.shortcuts import render
from .models import Pet

# Create your views here.
def Home(request):
    pets = Pet.objects.all()
    return render(request , 'Shelter/home.html' , {'pets' : pets})
