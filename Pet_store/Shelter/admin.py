from django.contrib import admin
from .models import Pet , Owner
# Register your models here.

@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('last_name',)
    list_display = ('first_name', 'last_name', 'phone', 'request_time')
    readonly_fields = ('request_time',)


@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    search_fields = ('name', 'species', 'owner__first_name', 'owner__last_name')
    list_display = ('name', 'species', 'age', 'available', 'owner')
    list_filter = ('available', 'species')