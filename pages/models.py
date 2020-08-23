from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.core.blocks import PageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    body = StreamField([
        ('subtitle', blocks.CharBlock(classname="full title")),
        ('section', blocks.StructBlock([
            ('heading', blocks.CharBlock()),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(required=False)),
            ('more_information', PageChooserBlock(required=False, help_text="Select a page where a member can find more information")),
        ])),
    ])
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request):
        # Update context to include only published events, ordered by reverse-chron
        context = super().get_context(request)
        eventspages = self.get_children().live().order_by('-first_published_at')
        paginator = Paginator(eventspages, 2)
        page = request.GET.get("page")
        try:
            eventspages = paginator.page(page)
        except PageNotAnInteger:
            eventspages = paginator.page(1)
        except EmptyPage:
            eventspages = paginator.page(paginator.num_pages)
        context['eventspages'] = eventspages
        return context

class GenericPage(Page):
    body = StreamField([
        ('subtitle', blocks.CharBlock(classname="full title")),
        ('section', blocks.StructBlock([
            ('heading', blocks.CharBlock()),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(required=False)),
            ('more_information', PageChooserBlock(required=False, help_text="Select a page where a member can find more information")),
        ])),
    ])
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class EventPage(Page):
    body = StreamField([
        ('subtitle', blocks.CharBlock(classname="full title")),
        ('section', blocks.StructBlock([
            ('heading', blocks.CharBlock()),
            ('date', blocks.DateTimeBlock()),
            ('location', blocks.RichTextBlock()),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(required=False)),
        ])),
    ])
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]