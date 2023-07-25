from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
from .forms import StatusForm
from django.urls import reverse_lazy

from .models import Order
from django.views.decorators.csrf import csrf_exempt


def your_number(request):
    order = Order.objects.last()
    return render(request, 'order/your_number.html', {'order': order})


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        order = random.randint(1, 2000)
        order_obj = Order.objects.filter(order_number=order).first()
        if order_obj:
            return JsonResponse({'error': 'Object Already Exist'})
        Order.objects.create(order_number=order, type=Order.CREATED_STATUS)
        return redirect('your_number')
    return render(request, 'order/create.html', {'warning': 'send post request to create new order'})


@csrf_exempt
def change_status_type(request, pk):
    order = Order.objects.get(pk=pk)
    form = StatusForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            handler_type_status = form.cleaned_data['type']
        order_obj = Order.objects.filter(order_number=order.order_number).first()
        if not order_obj:
            return JsonResponse({'error': 'Object Does not Exist'})
        order_obj.type = handler_type_status
        order_obj.save()
        return redirect('index')
    return render(request, 'order/change_order.html', {'order': order, 'form': form})


def order_page(request):
    orders = Order.objects.all()
    return render(request, 'order/index.html', {'order': orders})


def status_list(request):
    orders = Order.objects.all()
    return render(request, 'order/status_list.html', {'orders': orders})
