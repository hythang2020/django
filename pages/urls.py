from django.urls import path
from . import views

urlpatterns = [
    # Url to call to home_page function
    path('', views.home_page),
]
