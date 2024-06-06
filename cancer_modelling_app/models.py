from django.db import models

# Create your models here.
# models.py
from django.db import models

class SearchAnalytics(models.Model):
    keyword = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.keyword} at {self.timestamp}'
