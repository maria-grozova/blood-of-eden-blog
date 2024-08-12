from . import views
from django.urls import path

urlpatterns = [
    path('', views.StoriesList.as_view(), name='home'),
]