from django.db import models
from users.models import User

PUBLICATION_STATUS_CHOICES = [
    ('unpublished', 'Не опубликован'),
    ('draft', 'Черновик'),
    ('pending_review', 'Ожидает проверки'),
    ('published', 'Опубликован'),
]


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to="products/", verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения"),
    views_counter = models.PositiveIntegerField(default=0, verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров"),
    publication_status = models.CharField(max_length=20, choices=PUBLICATION_STATUS_CHOICES, default='unpublished')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец', help_text='Укажите владельца')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]

    def __str__(self):
        return self.name


class Group(models)