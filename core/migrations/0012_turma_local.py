# Generated by Django 3.1 on 2020-12-12 20:39

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_aluno_menor_de_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='local',
            field=mapbox_location_field.models.LocationField(default=(0, 0), map_attrs={'center': [17.031645, 51.106715], 'cursor_style': 'pointer', 'fullscreen_button': True, 'geocoder': True, 'marker_color': 'red', 'navigation_buttons': True, 'placeholder': 'Pick a location on map below', 'readonly': True, 'rotate': False, 'style': 'mapbox://styles/mapbox/outdoors-v11', 'track_location_button': True, 'zoom': 13}),
        ),
    ]
