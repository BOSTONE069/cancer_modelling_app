from django.contrib import admin

# Register your models here.
from .models import SearchAnalytics

@admin.register(SearchAnalytics)
class SearchAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('keyword',)