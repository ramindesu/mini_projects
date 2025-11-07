from django.urls import path
from .views import Home ,animal 

urlpatterns = [
    path('', Home, name='home'),
    path('animal/<int:pet_id>' ,animal ),

]