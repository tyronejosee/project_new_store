""""Actions for Utils App."""

from django.contrib import admin


class ActionsMixin(admin.ModelAdmin):
    """Mixin providing custom actions for showing and hiding elements."""

    actions = ["hide_elements", "show_elements"]

    @admin.action(description="Hide selected elements")
    def hide_elements(self, request, queryset):
        """Action to hide selected elements."""
        queryset.update(show_hide=False)

    @admin.action(description="Show selected elements")
    def show_elements(self, request, queryset):
        """Action to show selected elements."""
        queryset.update(show_hide=True)
