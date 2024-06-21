"""Models for Home App."""

from django.db import models
from cloudinary.models import CloudinaryField


class Company(models.Model):
    """Entity type model for Company."""
    name = models.CharField("Name", max_length=50)
    logo = CloudinaryField("Logo")
    copy = models.CharField("Copy", max_length=150)
    description = models.TextField("Description")
    email = models.EmailField("Email")
    github = models.URLField("GitHub")
    linkedin = models.URLField("LinkedIn")

    class Meta:
        ordering = ["name"]
        verbose_name = "company"
        verbose_name_plural = "company"
        app_label = "home"

    def __str__(self):
        return str(self.name)


class Page(models.Model):
    """Entity type model for Pages."""
    key = models.CharField("Unique Key", max_length=50, default="pending")
    content = models.TextField("Content", blank=True)
    image = CloudinaryField("Logo")
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        ordering = ["key"]
        verbose_name = "page"
        verbose_name_plural = "pages"
        app_label = "home"

    def __str__(self):
        return str(self.key)
