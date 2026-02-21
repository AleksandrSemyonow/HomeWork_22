from config.settings import CACHE_ENABLED
from catalog.models import Product
from django.core.cache import cache


def get_product_from_cache():
    """Получает данные по продуктам из кеша, если кеш пустой, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    """Получаем данные по продуктам выбранной категории из кеша, если кеш пустой, получаем данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    key = f"products_by_category_{category_id}"
    products = cache.get(key)

    if products is not None:
        return products
    products = Product.objects.filter(category_id=category_id)
    cache.set(key, products)
    return products
