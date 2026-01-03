from django.db import models

class Products(models.Model):
    name_products = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    describition = models.TextField()
    TYPE_PRODUCTS = (
        ("Education", "Education"),
        ("Travel", "Travel")
    )
    type_priducts = models.CharField(max_length=100, choices=TYPE_PRODUCTS, default="Education")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_products   # Выводим функцию (name_products) в админ панель