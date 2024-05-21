from django.urls import path
from .views import get_make, get_car, get_detail


urlpatterns = [
    path('', get_make, name='get_make'),
    path('cars/<int:pk>', get_car, name='get_car'),
    path('detail/<int:pk>', get_detail, name='detail')
]