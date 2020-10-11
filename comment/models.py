from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel
from publication.models import Publication


class Comment(BaseModel):
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="Комментатор"
    )
    text = models.TextField()
    publication = models.ForeignKey(
        to=Publication,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="Публикация"
    )


class CommentToComment(BaseModel):
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.CASCADE,
        related_name="comment_to_comment",
        verbose_name="Комментатор"
    )
    answer_text = models.TextField()
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        related_name="comment_to_comment",
        verbose_name="на комментарий"
    )