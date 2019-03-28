from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name    
    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True
    )

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    
    name = models.CharField(max_length=255)
    
    description = models.TextField(
        blank=True,
        null=True,
        
    )
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    image = models.ImageField(
        upload_to='products',
        null=True, blank=True
    )
   
    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name