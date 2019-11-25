from django.db import models

# Create your models here.
class Currency (models.Model):
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    target_currency = models.ManyToManyField('core.Currency', related_name='rates' , through='core.CurrencyRate')


    def __str__(self):
        return self.abbreviation


class CurrencyRate(models.Model):
    currency1 = models.ForeignKey('core.Currency', on_delete=models.CASCADE , related_name='currency_rates1')
    currency2 = models.ForeignKey('core.Currency', on_delete=models.CASCADE , related_name='currency_rates2')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return   f'{self.currency1}, {self.currency2}, {self.date}'


