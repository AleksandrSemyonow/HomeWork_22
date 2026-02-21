from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name="Вентиляторы", description="Напольные вентиляторы")

        products = [
            {"name": "Aceline UWTF", "description": "Напольный вентилятор", "category": category, "price": 500},
            {"name": "Media FD", "description": "Напольный вентилятор", "category": category, "price": 1000}
        ]

        for product_add in products:
            product, created = Product.objects.get_or_create(**product_add)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Добавление продукта прошло успешно: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже добавлен: {product.name}'))
