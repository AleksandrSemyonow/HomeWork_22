from django.urls import path, include
from catalog.apps import CatalogConfig
from django.conf.urls.static import static
from django.conf import settings
from catalog.views import HomeView, ContactView, ProductListView, ProductDetail, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryProductListView
from django.views.decorators.cache import cache_page


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="index"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", cache_page(60)(ProductDetail.as_view()), name="products_detail"),
    path("products/create/", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
    path("products/<int:category_id>", CategoryProductListView.as_view(), name="category_products")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
