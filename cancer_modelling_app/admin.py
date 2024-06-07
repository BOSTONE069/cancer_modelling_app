from django.contrib import admin

# Register your models here.
from .models import SearchAnalytics, Contact, PerformanceMetric

@admin.register(SearchAnalytics)
class SearchAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('keyword',)
    
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')

admin.site.register(Contact, ContactAdmin)


@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ('metric_name', 'value', 'recorded_at')
    list_filter = ('metric_name', 'recorded_at')