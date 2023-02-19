from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        all_obj = Phone.objects.all().order_by('name')
    elif sort_by =='min_price':
        all_obj = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        all_obj = Phone.objects.all().order_by('-price')
    else:
        all_obj = Phone.objects.all()

    context = {
        'phones':all_obj
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    #phone = Phone.objects.filter(slug = slug).first()
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone':phone
    }
    return render(request, template, context)
    #return HttpResponse (f'{context} {slug}')
