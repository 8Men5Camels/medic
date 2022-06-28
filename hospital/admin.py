from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import (
    Direction,
    Doctor,
)


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_filter = ["direction"]
    search_fields = ["direction"]


@admin.register(Doctor)
class DirectionAdmin(admin.ModelAdmin):
    list_filter = ["directions"]
    search_fields = ["first_name", "last_name"]
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
    }
    list_display = (
        "first_name",
        "last_name",
        "get_directions",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("directions")

    def get_directions(self, obj):
        return ", ".join([p.direction for p in obj.directions.all()])

    get_directions.short_description = "directions"
