from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class genericPage(Page):
    banner_title = models.CharField(max_length=100, default='welcome to my genericPage')

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
    ]
