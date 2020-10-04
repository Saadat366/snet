from django.contrib import admin
from .models import *


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "description",
        "user",
        "deleted"
    ]
    fields = [
        "image",
        "description",
        "deleted",
        "user"
    ]