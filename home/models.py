"""Models for Home App."""

from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    """Entity type model for Pages."""

    title = models.CharField(max_length=200, unique=True, verbose_name='Title')
    content = RichTextField(blank=True, null=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Adds extra metadata to the Page model."""
        verbose_name_plural = "Pages"
        ordering = ['-created_at',]
    
    def __str__(self):
        return str(self.title)
