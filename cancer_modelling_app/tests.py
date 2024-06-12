from django.test import TestCase

# Create your tests here.
import unittest
from datetime import datetime
from .models import PerformanceMetric

class PerformanceMetricTestCase(unittest.TestCase):
    
    def test_str_method(self):
        metric = PerformanceMetric(metric_name="Test Metric", value=10.5)
        self.assertEqual(str(metric), "Test Metric - 10.5")
        
    def test_recorded_at_auto_now_add(self):
        metric = PerformanceMetric(metric_name="Test Metric", value=10.5)
        self.assertIsNotNone(metric.recorded_at)
        self.assertTrue(isinstance(metric.recorded_at, datetime))

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            metric = PerformanceMetric(metric_name="Test Metric", value=-10.5)
    
    def test_empty_metric_name(self):
        with self.assertRaises(ValueError):
            metric = PerformanceMetric(metric_name="", value=10.5)