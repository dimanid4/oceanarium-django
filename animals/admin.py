from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'is_animal_of_the_day')
    list_filter = ('is_animal_of_the_day',)

from django.contrib import admin

admin.site.site_header = "Админ панель - Oceanarium 2025"
admin.site.site_title = "Oceanarium admin"
admin.site.index_title = "Управление океанариумом"
