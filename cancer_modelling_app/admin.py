from django.contrib import admin

# Register your models here.
from .models import SearchAnalytics, Contact, PerformanceMetric

# The code snippet you provided is registering the `SearchAnalytics` model with the Django admin site.
# By using the `@admin.register(SearchAnalytics)` decorator, you are telling Django to use the
# `SearchAnalyticsAdmin` class to customize the admin interface for the `SearchAnalytics` model.
@admin.register(SearchAnalytics)
class SearchAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('keyword',)
    
    
# The ContactAdmin class defines the display and search fields for the Contact model in the Django
# admin interface.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')

admin.site.register(Contact, ContactAdmin)


# The code snippet you provided is registering the `PerformanceMetric` model with the Django admin
# site. By using the `@admin.register(PerformanceMetric)` decorator, you are telling Django to use the
# `PerformanceMetricAdmin` class to customize the admin interface for the `PerformanceMetric` model.
@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ('metric_name', 'value', 'recorded_at')
    list_filter = ('metric_name', 'recorded_at')