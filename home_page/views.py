from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.


class HomeListView(ListView):
    template_name = 'home.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 1
