from django.conf import settings
from django.db import models

from django.utils.translation import gettext_lazy as _


GENRE_CHOICES = (
    ('HORROR', _('horror')),
    ('COMEDY', _('comedy')),
    ('ROMANCE', _('romance')),
    ('DRAMA', _('drama')),
    ('SCIFI', _('scifi')),
    ('ACTION', _('action')),
    ('MISCELLANEOUS', _('miscellaneous'))
)

class Film(models.Model):
    """films model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES, default='MISCELLANEOUS')
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title