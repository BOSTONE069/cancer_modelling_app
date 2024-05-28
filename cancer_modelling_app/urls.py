

from django.urls import path
from .views import publications_view

urlpatterns = [
    path('', publications_view, name='publications'),
]
