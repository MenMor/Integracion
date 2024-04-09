from django.urls import path
from .views import employee_form, success, download_csv

urlpatterns = [
    path('', employee_form, name='employee_form'),
    path('success/', success, name='success'),
    path('download-csv/', download_csv, name='download_csv'),
]
