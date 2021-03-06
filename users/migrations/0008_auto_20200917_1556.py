# Generated by Django 3.1 on 2020-09-17 18:56

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_custom_user_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='local',
            field=mapbox_location_field.models.LocationField(default=(0, 0), map_attrs={'center': [17.031645, 51.106715], 'cursor_style': 'pointer', 'fullscreen_button': True, 'geocoder': True, 'marker_color': 'red', 'navigation_buttons': True, 'rotate': False, 'style': 'mapbox://styles/mapbox/outdoors-v11', 'track_location_button': True, 'zoom': 13}),
        ),
    ]
