from django.test import TestCase
from django.utils import timezone
# Create your tests here.
import unittest
from datetime import datetime
from .models import PerformanceMetric, Contact

# The `PerformanceMetricTestCase` class contains test methods for a `PerformanceMetric` class,
# covering string representation, auto timestamp, negative value handling, and empty metric name
# validation.
class PerformanceMetricTestCase(unittest.TestCase):
    
    def test_str_method(self):
        """
        The function `test_str_method` tests the string representation of a `PerformanceMetric` object.
        """
        metric = PerformanceMetric(metric_name="Test Metric", value=10.5)
        self.assertEqual(str(metric), "Test Metric - 10.5")
        
    def test_recorded_at_auto_now_add(self):
        """
        The function tests that the recorded_at attribute of a PerformanceMetric instance is
        automatically set to the current datetime upon creation.
        """
        metric = PerformanceMetric(metric_name="Test Metric", value=10.5)
        self.assertIsNotNone(metric.recorded_at)
        self.assertTrue(isinstance(metric.recorded_at, datetime))

    def test_negative_value(self):
        """
        The function `test_negative_value` tests that a `ValueError` is raised when a negative value is
        passed to the `PerformanceMetric` constructor.
        """
        with self.assertRaises(ValueError):
            metric = PerformanceMetric(metric_name="Test Metric", value=-10.5)
    
    def test_empty_metric_name(self):
        """
        The function tests for an empty metric name by raising a ValueError if the metric name is empty.
        """
        with self.assertRaises(ValueError):
            metric = PerformanceMetric(metric_name="", value=10.5)
            
            
class ContactTestCase(unittest.TestCase):

    def test_contact_creation(self):
        contact = Contact.objects.create(name="John Doe", email="johndoe@example.com", subject="Test Subject", message="Test Message")
        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.email, "johndoe@example.com")
        self.assertEqual(contact.subject, "Test Subject")
        self.assertEqual(contact.message, "Test Message")
        self.assertTrue(contact.created_at <= timezone.now())

    def test_contact_str_method(self):
        contact = Contact.objects.create(name="Jane Smith", email="janesmith@example.com", subject="Another Subject", message="Another Message")
        self.assertEqual(str(contact), "Jane Smith")

    def test_invalid_email(self):
        with self.assertRaises(Exception):
            Contact.objects.create(name="Invalid Email", email="invalidemail", subject="Invalid Subject", message="Invalid Message")
