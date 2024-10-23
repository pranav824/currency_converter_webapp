from django.db import models

class ConversionHistory(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    amount = models.FloatField()
    converted_amount = models.FloatField()
    conversion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.from_currency} to {self.to_currency} = {self.converted_amount} on {self.conversion_date}"
