# Generated by Django 3.0.8 on 2021-01-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210119_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='suffix',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos'),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]