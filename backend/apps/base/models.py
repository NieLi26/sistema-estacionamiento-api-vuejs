from django.db import models
from django.conf import settings

from pytz import timezone
from datetime import datetime

# Create your models here.

class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    is_active = models.BooleanField('Activo', default=True)
    created_at = models.DateField('Fecha de Creación', auto_now_add=True)
    modified_at = models.DateField('Fecha de Modificaión', auto_now=True)

    class Meta:
        """Meta definition for BaseModel."""

        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
