# Save Methods
def save(self, *args, **kwargs):
    # Rename the image associated with the page
    if self.image and self.image.name:
        if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
            file_name, file_extension = os.path.splitext(self.image.name)
            file_name = f"{self.key}{file_extension}"
            self.image.name = file_name
    super(Page, self).save(*args, **kwargs)


@receiver(post_delete, sender=Product)
def product_remove_image(sender, instance, **kwargs):
    """Signal to remove the related image when deleting a product."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(post_delete, sender=Deal)
def deal_remove_image(sender, instance, **kwargs):
    """Signal to remove the related image when deleting a deal."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


# Rename the image associated with the product
if self.image and self.image.name:
    if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
        file_name, file_extension = os.path.splitext(self.image.name)
        title = self.slug[:100]
        file_name = f"{title}{file_extension}"
        self.image.name = file_name


# Rename the image associated with the deal
if self.image and self.image.name:
    if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
        file_name, file_extension = os.path.splitext(self.image.name)
        title = self.slug[:100]
        file_name = f"{title}{file_extension}"
        self.image.name = file_name


def save_model(self, request, obj, form, change):
    # Remove the image when clearing the path on the page
    if change and "image" in form.changed_data:
        old_page = Page.objects.get(pk=obj.pk)
        old_page.image.delete(save=False)
    super().save_model(request, obj, form, change)

# Database Settings
DATABASE_URL=postgres://postgres:bernardoreyes@127.0.0.1:5432/new_store

# Github Actions
DB_NAME: ${{ secrets.DB_NAME }}
DB_USER: ${{ secrets.DB_USER }}
DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
DB_HOST: ${{ secrets.DB_HOST }}
DB_PORT: ${{ secrets.DB_PORT }}