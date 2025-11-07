from django.urls import path
from .views import Home, animal, adopt

urlpatterns = [
    path("", Home, name="home"),
    path("animal/<int:pet_id>", animal),
    path("adopt/<int:pet_id>", adopt, name="adopt_pet"),
    
]
