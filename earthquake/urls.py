from django.urls import path
from . import views

urlpatterns = [
    path('earthquake/', views.earthquake_data, name='earthquake_data'),
]
