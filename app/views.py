from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')
    #return HttpResponse('Hello world !!')


def product(request):
    data = {
        "products":[{
            "name": "Tivi 01",
            "price": "20.000",
        },
        {
            "name": "Tivi 02",
            "price": "50.000",
        },{
            "name": "Tivi 03",
            "price": "70.000",
        },
        ]
    }
    return render(request, 'product.html',data)
    #return HttpResponse('Product list view !!!')