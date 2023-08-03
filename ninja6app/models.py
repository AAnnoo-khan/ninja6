from django.db import models

# Create your models here.

class Quotetion(models.Model):
    Quote = models.CharField(max_length=260)
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=models.CASCADE)
    # author = 

    def __str__(self):
        return self.Quote

    def snippet(self):
        return self.details[:60]+'...'