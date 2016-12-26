# -*- coding: utf-8 -*-
from django import forms

from beykam.models import Personnel, Category, Product, PurchaseActivity, SaleActivity, Supplier, Inventory


class SignInForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)


class PersonnelAddForm(forms.ModelForm):
    class Meta:
        model = Personnel
        exclude = ()
        labels = {
            'fullname': 'İsim Soyisim',
            'phone': 'Telefon',
            'email': 'E-posta',
            'photo': 'Fotoğraf',
            'address': 'Adres',
            'house': 'İkametgah',
            'marital_status': 'Medeni Hali',
            'children': 'Çocuk',
            'tax_exemption': 'Vergi Muafiyet Belgesi var mı?',
            'cut': 'Maliyet Kesintisi',
            'paid_price': 'Ödenen Miktar',
        }
        help_texts = {
            'cut': 'Maliyet kesintisini oranı yüzde (%) olarak kabul edilir',
            'tax_exemption': 'Var ise işaretleyiniz',
            'paid_price': 'Üreticiye ne kadar ödeme yapıldığını yazabilirsiniz'
        }


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ()
        labels = {
            'name': 'Şablon İsmi',
        }


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()
        labels = {
            'name': 'Ürün İsmi',
            'category': 'Şablon',
            'price': 'Fiyat',
        }


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseActivity
        exclude = ('total',)
        labels = {
            'product': 'Ürün',
            'personnel': 'Üretici',
            'count': 'Adet',
            'cut': 'Maliyet Kesintisi'
        }
        help_texts = {
            'count': 'Birden fazla alım kaydı girecekseniz adet belirtiniz',
            'cut': 'Maliyet kesintisini oranı yüzde (%) olarak kabul edilir',
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = SaleActivity
        exclude = ('total',)
        labels = {
            'product': 'Ürün',
            'personnel': 'Üretici',
            'discount': 'İndirim',
            'is_free': 'Ücretsiz mi ?',
            'count': 'Adet',
            'price': 'Satış Fiyatı'
        }
        help_texts = {
            'discount': 'İndirim var ise tutarı yüzde (%) olarak kabul edilir',
            'is_free': 'Ücretsiz ise işaretleyiniz',
            'count': 'Birden fazla satış kaydı girecekseniz adet belirtiniz',
            'price': 'Eğer indirim girmek istemezseniz satış fiyatını girebilirsiniz',
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ()
        labels = {
            'name': 'İşyeri Adı',
            'address': 'İşyeri Adresi',
            'phone': 'İşyeri Telefon',
            'email': 'İşyeri E-posta',
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ()
        labels = {
            'supplier': 'İşyeri',
            'quantity': 'Miktarı',
            'unit': 'Birimi',
            'price': 'Fiyat',
            'date': 'Tarih',
        }
        help_texts = {
            'unit': 'Örneğin kg, m, dm, g gibi birimler yazabilirsiniz',
        }
        widgets = {
            'date': DateInput(),
        }
