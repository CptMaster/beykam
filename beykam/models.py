from django.db import models
from django.utils.timezone import now

marital_choices = (('Evli', 'Evli'),
                   ('Bekar', 'Bekar'),
                   ('Dul', 'Dul'),
                   )


class Personnel(models.Model):
    fullname = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    photo = models.ImageField(upload_to='personnel', blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    house = models.CharField(max_length=255, null=True, blank=True)
    marital_status = models.CharField(max_length=255, null=True, blank=True, choices=marital_choices)
    children = models.CharField(max_length=255, null=True, blank=True)
    tax_exemption = models.BooleanField(default=0, blank=True)
    cut = models.DecimalField(default=30, max_digits=10, decimal_places=2)
    paid_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.fullname


class Product(models.Model):
    category = models.ForeignKey('Category')
    name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.category.name + " - " + self.name


class PurchaseActivity(models.Model):
    product = models.ForeignKey('Product')
    personnel = models.ForeignKey('Personnel')
    count = models.IntegerField(default=1)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class SaleActivity(models.Model):
    product = models.ForeignKey('Product')
    personnel = models.ForeignKey('Personnel')
    discount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    count = models.IntegerField(default=1)
    is_free = models.BooleanField(default=False)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class Supplier(models.Model):
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=False, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.name


class Inventory(models.Model):
    supplier = models.ForeignKey('Supplier')
    quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    date = models.DateField(null=True, blank=True, default=now().date())
