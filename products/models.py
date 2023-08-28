"""Products Models"""

from django.db import models
#from django.utils.decorators import method_decorator

class Category(models.Model):
    """
    Model representing a Category in the store.
    """
    category = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=250)
    show = models.BooleanField(default=True)

    def __str__(self):
        return str(self.category)

    class Meta:
        """
        Adds extra metadata to the Category model.
        """
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Image(models.Model):
    """
    Model representing a list of images in the products.
    """
    link = models.URLField()

    def __str__(self):
        return str(self.link)

    class Meta:
        """
        Adds extra metadata to the Image model.
        """
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Currency(models.Model):
    """
    Model representing currency types in the store.
    """
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)

    class Meta:
        """
        Adds extra metadata to the currency model.
        """
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Product(models.Model):
    """
    Model representing a product in the store.
    """
    date = models.DateTimeField(auto_now_add=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    detail = models.JSONField()
    show = models.BooleanField(default=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    class Meta:
        """
        Adds extra metadata to the Product model.
        """
        verbose_name = "Product"
        verbose_name_plural = "Products"
