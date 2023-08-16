from django.urls import path
from . import views

urlpatterns = [
    path('', views.earthquake_data, name='earthquake_data'),
]
