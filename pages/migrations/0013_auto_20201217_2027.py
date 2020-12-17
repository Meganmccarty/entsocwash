# Generated by Django 3.0.8 on 2020-12-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20201217_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', help_text='Add a title for this specific meeting.', max_length=100)),
                ('date', models.DateTimeField(help_text='Enter the date and time of the meeting.')),
                ('meeting_details', models.TextField(default='', help_text='Include the specifics of the meeting')),
                ('image', models.ImageField(blank=True, help_text='Optional; select an image to go with this meeting.', null=True, upload_to='')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]