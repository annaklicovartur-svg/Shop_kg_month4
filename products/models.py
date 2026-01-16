from django.db import models

class Products(models.Model):
    name_products = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    describition = models.TextField()
    TYPE_PRODUCTS = (
        ("Education", "Education"),
        ("Travel", "Travel")
    )
    type_products = models.CharField(max_length=100, choices=TYPE_PRODUCTS, default="Education")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name_products   # Выводим функцию (name_products) в админ панель

class Reviews(models.Model):
        #Related_name = аналог кекстного ключа, когда мы хотим получить все коменты к какому то обьекту мы обращаемся k related_name
        choice_product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="review")
        MARKS = (
            ("⭐", "⭐"),
            ("⭐⭐", "⭐⭐"),
            ("⭐⭐⭐", "⭐⭐⭐"),
            ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
            ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐")
        )
        marks = models.CharField(max_length=100, choices=MARKS, default="⭐⭐⭐⭐")
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.choice_product} : {self.marks}"  # Произвел миграцию