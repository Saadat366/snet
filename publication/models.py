from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel


class Publication(BaseModel):
    publisher = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="publication",
        verbose_name="Автор"
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="publications",
        verbose_name="Изображение"
    )


class Hashtag(BaseModel):
    publication = models.ManyToManyField(
        to=Publication,
        blank=True,
        related_name="hashtag",
        verbose_name="Хэштег"
    )


class Like(BaseModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="like",
        verbose_name="От"
    )
    publication = models.ForeignKey(
        to=Publication,
        on_delete=models.CASCADE,
        related_name="like",
        verbose_name="Публикации"
    )