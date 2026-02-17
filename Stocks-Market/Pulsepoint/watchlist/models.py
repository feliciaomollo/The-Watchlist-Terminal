from django.db import models

# Create your models here.
class watchlistTerminal(models.Model):
    ticker = models.CharField(max_length=40)
    company_name = models.CharField(max_length=40)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__ (self):
        return self.ticker