from django.db import models


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=True,
        unique=True,
        editable=False,
        db_index=True
    )

    class Meta:
        abstract = True