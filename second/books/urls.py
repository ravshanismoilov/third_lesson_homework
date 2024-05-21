from django.urls import path
from .views import *


urlpatterns = [
    path('', get_info, name='get_info'),
    path('product/<int:pk>', get_books, name='get_books'),
    path('product/detail/<int:pk>', get_detail, name='get_detail')
]