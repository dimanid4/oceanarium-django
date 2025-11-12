from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if getattr(obj, "image", None):
            try:
                return format_html('<img src="{}" style="max-height:140px; border-radius:8px"/>', obj.image.url)
            except Exception:
                return "—"
        return "—"

    preview.short_description = "Превью"

from django.contrib import admin

admin.site.site_header = "Админ панель - Oceanarium 2025"
admin.site.site_title = "Oceanarium admin"
admin.site.index_title = "Управление океанариумом"
