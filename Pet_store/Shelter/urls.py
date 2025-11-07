from django.urls import path
from .views import Home, animal, adpot

urlpatterns = [
    path("", Home, name="home"),
    path("animal/<int:pet_id>", animal),
    path("adopt/<int:pet_id>", adpot, name="adopt_pet"),
    
]
