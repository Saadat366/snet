from django.contrib import admin
from .models import *


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "likes",
        "description",
        "publisher",
        "updated",
        "deleted"
    ]
    fields = [
        "image",
        "likes",
        "description",
        "deleted",
        "publisher",
    ]

    def likes(self, obj):
        return obj.like.count()


@admin.register(Hashtag)
class Hashtag(admin.ModelAdmin):
    list_display = [
        "name",
        "publication_count"
    ]

    def publication_count(self, obj):
        return obj.publication.count()


# @admin.register(Like)