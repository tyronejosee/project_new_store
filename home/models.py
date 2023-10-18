"""Models for Home App."""

from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    """Entity type model for Pages."""

    key = models.CharField(
        max_length=50, default='pending', verbose_name='Unique Key')
    content = RichTextField(blank=True, null=True, verbose_name='Content')
    image = models.ImageField(
        upload_to='pages/', null=True, verbose_name='Image')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Adds extra metadata to the Page model."""
        verbose_name_plural = "Pages"
        ordering = ['-created_at',]

    def __str__(self):
        return str(self.key)
