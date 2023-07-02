from django.urls import path
from .viewsets import NaicsSearchView

urlpatterns = [
    path('', NaicsSearchView.as_view({'get': 'list'}), name='naics-search'),
]
