from django.urls import path
from .views import ReviewToPage

urlpatterns = [
    path('review', ReviewToPage.as_view(), name='review')
]

