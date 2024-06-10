# middleware.py

import time
from .models import PerformanceMetric

# The `PerformanceMetricMiddleware` class measures the duration of each request and stores it in a
# database as a performance metric.
class PerformanceMetricMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        PerformanceMetric.objects.create(metric_name='request_duration', value=duration)

        return response
