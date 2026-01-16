from django.db import models

class Basket(models.Model):
    buy_choice = models.CharField(max_length=100, verbose_name='Enter name of the product')
    STATUS_BS = (
        ('BUY', 'BUY'),
        ('NOT_BUY', 'NOT_BUY')
    )
    status_bs = models.CharField(max_length=100, verbose_name='enter your status', choices=STATUS_BS, default='NOT_BUY')
                            
    def __str__(self):
        return f'{self.buy_choice}-{self.status_bs}'

    class Meta:
        verbose_name = 'basket'
        verbose_name_plural = 'baskets'