from django.urls import path, include
from catalog.apps import CatalogConfig
from django.conf.urls.static import static
from django.conf import settings
from catalog.views import home, contacts, products_list, products_detail


app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="index"),
    path("contacts/", contacts, name="contacts"),
    path("products/", products_list, name="products_list"),
    path("products/<int:pk>/", products_detail, name="products_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
