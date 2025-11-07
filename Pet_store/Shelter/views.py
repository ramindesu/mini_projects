from django.http import HttpResponse
from django.shortcuts import render
from .models import Pet
from .forms import OwnerForms

# Create your views here.
def Home(request):
    pets = Pet.objects.filter(available = True)
    return render(request, "Shelter/home.html", {"pets": pets})


def animal(request, pet_id):
    pet = Pet.objects.get(id = pet_id)
    return render(request, 'Shelter/animal.html' , {'pet':pet})

def adpot(request,pet_id):
    if request.method == "POST":
        form = OwnerForms(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponse('adoption succesful')
    else:
        form= OwnerForms()

    return render(request , 'adoption.html' , {'form':form})