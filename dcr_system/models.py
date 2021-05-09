from django.db import models


class ProductType(models.Model):
    product_type_name = models.CharField(max_length=250)

    def __str__(self):
        return self.product_type_name


class ProductInformation(models.Model):
    product_name = models.CharField(max_length=250)
    product_price = models.FloatField()
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='product_type')

    def __str__(self):
        return self.product_name
