from django.db import models

# Create your models here.
# models.py
from django.db import models

# The `SearchAnalytics` class represents a model with fields for keyword and timestamp in a Django
# application.
class SearchAnalytics(models.Model):
    keyword = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.keyword} at {self.timestamp}'


# This Python class defines a model for storing contact information including name, email, subject,
# message, and creation timestamp.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# The `PerformanceMetric` class defines a model with fields for metric name, value, and recorded
# timestamp in a Django application.
class PerformanceMetric(models.Model):
    metric_name = models.CharField(max_length=100)
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_name} - {self.value}"