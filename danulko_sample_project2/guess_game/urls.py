from django.urls import path
from .views import guess_number

urlpatterns = [
    path('', guess_number, name='guess'),
]
