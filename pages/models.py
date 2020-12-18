from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.core.blocks import PageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    body = StreamField([
        ('subtitle', blocks.CharBlock(classname="full title", help_text="Enter a subtitle for the page")),
        ('section', blocks.StructBlock([
            ('heading', blocks.CharBlock(help_text="Enter a heading for a section of text on the page")),
            ('text', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(required=False)),
        ])),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        # Update context to include only published events, ordered by reverse-chron
        context = super().get_context(request)
        upcoming_meetings = Meeting.objects.filter(date__gte=timezone.now()).order_by('-date')
        context['upcoming_meetings'] = upcoming_meetings
        return context

class GenericPage(Page):
    body = StreamField([
        ('subtitle', blocks.CharBlock(classname="full title")),
        ('section', blocks.StructBlock([
            ('heading', blocks.CharBlock(required=False)),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(required=False)),
            ('more_information', PageChooserBlock(required=False, help_text="Select a page where a member can find more information")),
        ])),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class Meeting(models.Model):
    title = models.CharField(default='', max_length=100, help_text="Add a title for this specific meeting")
    date = models.DateTimeField(help_text="Enter the date and time of the meeting")
    location = models.CharField(default='', max_length=500, help_text="Enter the location of the meeting")
    meeting_details = models.TextField(default='', help_text="Include the specifics of the meeting")
    image = models.ImageField(upload_to='meeting_images/', null=True, blank=True, help_text="Optional; select an image to go with this meeting")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title