from django.urls import path
from .views import create_order, change_status_type, order_page, your_number, status_list

urlpatterns = [
    path('', order_page, name='index'),
    path('create_order', create_order, name='create'),
    path('change_status_type/<int:pk>', change_status_type, name='change_status'),
    path('status_list/', status_list, name='status_list'),
    path('order/', your_number, name='your_number')

]
