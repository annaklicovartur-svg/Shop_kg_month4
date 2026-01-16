from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect  
from .forms import BasketForm  
from .models import Basket

def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/basket_list/')
    else:
        form = BasketForm()

    return render(
        request,
        template_name='basket/choice_bs.html',
        context={"form": form}
    )

def read_basket_view(request):
    if request.method == 'GET':
        basket = Basket.objects.all()
    return render(request, template_name='basket/basket_list.html',
                  context={'basket': basket})

def delete_basket_view(request, id):
    basket_id = get_object_or_404(Basket, id=id)
    basket_id.delete()
    return redirect('/basket_list/')
