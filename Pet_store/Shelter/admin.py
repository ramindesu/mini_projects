from django.contrib import admin
from .models import Pet , Owner
# Register your models here.

@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    search_fields = ('first_name',)
    list_filter = ('last_name' , )
    fields = ('first_name' , 'last_name')
@admin.register(Pet)
class AdminPet(admin.ModelAdmin):

    search_fields = ('name',)
