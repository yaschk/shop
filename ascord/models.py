from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):

            return '%s ' % self.name

    class Meta:
         verbose_name= "Категория товара"
         verbose_name_plural = "Категории товаров"


class Product(models.Model):

    product_name = models.CharField(max_length=130, blank=True, null=True, default=None)
    price = models.CharField(max_length=20, blank=True, null=True, default=0.00)
    in_stock = models.CharField(max_length=50, blank=True, null=True, default=0)
    add_info = models.CharField(max_length=50, blank=True, null=True, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    
    def __str__(self):

        return '%s ' % self.product_name

    class Meta:
         verbose_name= "Товар"
         verbose_name_plural = "Товары"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='static/media/products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):

             return '%s ' % self.id

    class Meta:
         verbose_name= "Фотография"
         verbose_name_plural = "Фотографии"
