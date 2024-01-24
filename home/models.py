"""Models for Home App."""

import os
from django.db import models
from utils.validators import validate_extension


class Company(models.Model):
    """Entity type model for Company."""
    name = models.CharField(max_length=50, verbose_name='Name')
    logo = models.FileField(upload_to='company/', verbose_name='Logo')
    copy = models.CharField(max_length=150, verbose_name='Copy')
    description = models.TextField(verbose_name='Description')
    email = models.EmailField(verbose_name='Email')
    github = models.URLField(verbose_name='GitHub')
    linkedin = models.URLField(verbose_name='LinkedIn')

    class Meta:
        """Meta definition for Company model."""
        verbose_name_plural = "Company"

    def __str__(self):
        return str(self.name)


class Page(models.Model):
    """Entity type model for Pages."""
    key = models.CharField(max_length=50, default='pending', verbose_name='Unique Key')
    content = models.TextField(blank=True, null=True, verbose_name='Content')
    image = models.FileField(upload_to='pages/', validators=[validate_extension], blank=True, null=True, verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Meta definition for Page model."""
        verbose_name_plural = "Pages"
        ordering = ['-created_at',]

    def __str__(self):
        return str(self.key)

    def save(self, *args, **kwargs):
        # Rename the image associated with the page
        if self.image and self.image.name:
            if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
                file_name, file_extension = os.path.splitext(self.image.name)
                file_name = f'{self.key}{file_extension}'
                self.image.name = file_name

        super(Page, self).save(*args, **kwargs)
