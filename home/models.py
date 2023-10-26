"""Models for Home App."""

import os
from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    """Entity type model for Pages."""

    key = models.CharField(
        max_length=50, default='pending', verbose_name='Unique Key')
    content = RichTextField(blank=True, null=True, verbose_name='Content')
    image = models.ImageField(
        upload_to='pages/', blank=True, null=True, verbose_name='Image')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Adds extra metadata to the Page model."""
        verbose_name_plural = "Pages"
        ordering = ['-created_at',]

    def __str__(self):
        return str(self.key)

    def save(self, *args, **kwargs):
        """Override the save method to rename the image before saving it."""
        if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
            # Gets the original file name
            file_name, file_extension = os.path.splitext(self.image.name)
            # Creates the new name in the format 'visual-key.webp'
            new_file_name = f'visual-{self.key}{file_extension}'
            # Changes the file name
            self.image.name = new_file_name

        super(Page, self).save(*args, **kwargs)
