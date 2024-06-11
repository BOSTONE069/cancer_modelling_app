

from django.urls import path, include
from .views import *
from .admin import SearchAnalyticsAdmin

urlpatterns = [
    path('', homepage, name='homepage'),
    path('publications/', publications_view, name='publications'),
    path('publications/search/<str:keyword>/', publications_view, name='publications_search'),
    path('contact/', contacts, name='contact'),
    path('silk/', include('silk.urls', namespace='silk')),
    path('admin/search_analytics/', SearchAnalyticsAdmin.changelist_view),
]
