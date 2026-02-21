from django.forms import ModelForm, BooleanField
from catalog.models import Product, Category
from django.core.exceptions import ValidationError


forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                   'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
            self.fields['description'].widget.attrs.update({'class': 'form_control', 'placeholder': 'Описание продукта'})
            self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Загрузите фото'})
            self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите категорию товара'})
            self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена товара'})

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if any(word in name.lower() for word in forbidden_words):
                raise ValidationError('В названии продукта не должно быть запрещенных слов!')
            return name

        def clean_description(self):
            description = self.cleaned_data.get('description')
            if any(word in description.lower() for word in forbidden_words):
                raise ValidationError('В описании продукта не должно быть запрещенных слов!')
            return description

        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price < 0:
                raise ValidationError('Цена не может быть отрицательной!')
            return price


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
