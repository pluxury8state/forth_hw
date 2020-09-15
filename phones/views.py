from django.shortcuts import render
from pprint import pprint
from .models import Phone
from .management.commands.import_phones import Command


command = Command()

# command.handle()

response = command.get_phones()


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'max_price':
        val = Phone.objects.order_by('-price')
        context = {
            'phones': val,
            'sort': sort
        }
        return render(request, template, context)
    elif sort == 'min_price':
        val = Phone.objects.order_by('price')
        context = {
            'phones': val,
            'sort': sort
        }
        return render(request, template, context)
    elif sort == 'name':

        val = Phone.objects.order_by('name')
        context = {
            'phones': val,
            'sort': sort
        }
        return render(request, template, context)
    val = Phone.objects.order_by('price')
    context = {
        'phones': val,
        'sort': sort
    }
    return render(request, template, context)


def show_product(request, slug: str):
    print(slug)

    template = 'product.html'
    # slug = slug.replace('-', ' ')
    context = {
        'product': Phone.objects.filter(name__icontains=slug).first()
    }
    return render(request, template, context)