from typing import Dict, Any
from django.urls import reverse_lazy, reverse
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import CategoryForm, ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model = Product


class ContactView(ListView):
    model = Product


class ProductListView(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
