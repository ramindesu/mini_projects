from django.contrib import admin
from .models import Pet , Owner
# Register your models here.
@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    pass
@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    pass
