from typing import Dict, Any
from django.urls import reverse_lazy, reverse
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import CategoryForm, ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from catalog.services import get_product_from_cache, get_products_by_category


class HomeView(ListView):
    model = Product


class ContactView(ListView):
    model = Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache()


class ProductDetail(DetailView):
    model = Product

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_counter += 1
    #     self.object.save()
    #     return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save(commit=False)
        product.published = True
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.can_delete_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


class CategoryProductListView(ListView):
    model = Product
    template_name = "catalog/category_product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return get_products_by_category(category_id)
