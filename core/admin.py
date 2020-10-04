from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["id",
        "user",
        "created",
        "updated",
        "deleted"
    ]
    fields = ["user"]