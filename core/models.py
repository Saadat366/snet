from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Название"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения"
    )
    deleted = models.BooleanField(
        default=False,
        verbose_name="Удалено"
    )

    def __str__(self):
        if self.name:
            return self.name
        return f"Объект{self.pk}"

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(
        to=User,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="profile",
        verbose_name="Пользователь"
    )
    subscription = models.ManyToManyField(
        to=User,
        blank=True,
        related_name="subscriber",
        verbose_name="Подписка"
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="О профиле"
    )
    profile_photo = models.ImageField(
        default="default_pic.jpg/",
        upload_to="profiles"
    )