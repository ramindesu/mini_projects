from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404 ,redirect
from .models import Pet
from .forms import OwnerForms

# Create your views here.
def Home(request):
    pets = Pet.objects.filter(available = True)
    return render(request, "Shelter/home.html", {"pets": pets})


def animal(request, pet_id):
    pet = Pet.objects.get(id = pet_id)
    return render(request, 'Shelter/animal.html' , {'pet':pet})

def adopt(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    # if pet.available is False:
    #     return HttpResponse('This pet is already adopted. bro')

    if request.method == "POST":
        form = OwnerForms(request.POST)
        if form.is_valid():
            owner = form.save()
            pet.owner = owner
            pet.available = False
            pet.save()
            return redirect('home')
    else:
        form = OwnerForms()

    return render(request, 'Shelter/adoption.html', {'form': form, 'pet': pet})