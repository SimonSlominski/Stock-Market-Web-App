from django.db import models


class StockTickers(models.Model):
    ticker = models.CharField(max_length=20)

    def __str__(self):
        return self.ticker
