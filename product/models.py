from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.TextField(blank=True, null=True)
    description = models.TextField()
    parent_id = models.ForeignKey(Category, blank=True, null=True)
    image = models.TextField()
    is_active = models.BooleanField()
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

class Product(models.Model):
    category_id = models.ForeignKey(Category)
    name = models.CharField()
    slug = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    stock_quantity = models.IntegerField()
    sku = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=300)
    image = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

