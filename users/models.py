from django.db import models
from django.contrib.auth.models import AbstractUser
from mapbox_location_field.models import LocationField
import datetime
from django.utils import timezone
# Create your models here.


class custom_user(AbstractUser):
    # 1 -> motorista
    # 2 -> aluno
    permissao = models.IntegerField(default=2)
    telefone = models.CharField(max_length=50,  default='1')
    local = LocationField(default=(0, 0), null=False, map_attrs={
        "style": "mapbox://styles/mapbox/outdoors-v11",
        "zoom": 13,
        "center": [17.031645, 51.106715],
        "cursor_style": 'pointer',
        "marker_color": "red",
        "rotate": False,
        "geocoder": True,
        "fullscreen_button": True,
        "navigation_buttons": True,
        "track_location_button": True,
        "readonly": True,
        "placeholder": "Pick a location on map below",
    })
    data_nascimento = models.DateField(
        auto_now=False, auto_now_add=False, null=False, blank=False, default=timezone.now())
