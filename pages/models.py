from django.db import models

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
