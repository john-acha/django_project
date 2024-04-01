# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView # New

urlpatterns = [
	path('about/', AboutPageView.as_view(), name='about'), # New
	path('', HomePageView.as_view(), name='home'),
]