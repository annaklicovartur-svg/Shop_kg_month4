from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products
from datetime import datetime

def products(request):
    if request.method == "GET":
        products = Products.objects.all()
    return render(
        request,
        template_name='products/products_list.html',
        context={
            'products': products
        }
    )

def products_detail(request, id):
    if request.method == "GET":
        products_id = get_object_or_404(Products, id=id)
    return render(
        request,
        template_name='products/products_detail.html',
        context={
            'products_id': products_id
        }
    )


def food(request):
    if request.method == "GET":
        return HttpResponse("1. Ramen\n 2. Sushi\n 3. Icecream")

def timeset(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html_content = f"""
        <h3>Текущая дата и время:</h3>
        <p>{current_time}</p>
        <hr>
        <h3>Фотка и текст о себе:</h3>
        <img src="https://blog.100ct.by/wp-content/uploads/2023/02/1-7.webp">
        <p>Меня зовут Артур мне 16 лет, занимаюсь программированием в учебной академии GEEKS на 4 месяце обучения</p>
        """
        return HttpResponse(html_content)