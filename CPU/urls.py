from .views import *
from django.urls import path

urlpatterns = [
    path('cpu/', cpu, name='cpu'),
    path('get_all_cpus/', get_all_cpus, name='get_all_cpus'),
]