from django.contrib import admin

# Register your models here.
from vakansii.models import Vacansii

@admin.register(Vacansii)
class VacansiiAdmin(admin.ModelAdmin):
    """Ваканции"""
    list_display = (
        "owner",
        "job_title",
        "requirement",
        "responsibilities",
        "terms",
        "income",
        "city",
        "contact_person",
        "created_at",
        "updated_at",
        "slug"
    )

    list_display_links = ("job_title",)
    list_filter = ("owner", "job_title", "created_at")
    prepopulated_fields = {"slug": ("owner", "job_title")}
    search_fields = ("owner", "job_title")
