from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=25, unique=True)
    description = models.TextField()
    show = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Image(models.Model):
    link = models.URLField()

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    #category_id = models.OneToOneField(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    detail = models.JSONField()
    show = models.BooleanField(default=True)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    #admin_id = models. ForeignKey(Admin, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        abstract = True
