# Generated by Django 3.0.8 on 2020-12-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20201217_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_details',
            field=models.TextField(default='', help_text='Include the specifics of the event'),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional; select an image to go with this event.', null=True, upload_to=''),
        ),
    ]
