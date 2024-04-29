from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image=models.ImageField(upload_to="categories")


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete= models.CASCADE ,related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()




class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productimages")
    image = models.ImageField(upload_to='product')