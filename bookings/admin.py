from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'number_of_people', 'created_at')
    list_filter = ('date',)

admin.site.site_header = "Админ панель - Oceanarium 2025"
admin.site.site_title = "Oceanarium admin"
admin.site.index_title = "Управление океанариумом"