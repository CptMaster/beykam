# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from beykam.forms import SignInForm, PersonnelAddForm, CategoryAddForm, ProductAddForm, PurchaseForm, SaleForm, \
    SupplierForm, InventoryForm
from beykam.models import Personnel, Category, Product, PurchaseActivity, SaleActivity, Supplier, Inventory


@login_required()
def homepage(request):
    personnal = Personnel.objects.all()
    total_personnal = personnal.count()
    total_personnal_price = 0
    for p in personnal:
        total_personnal_price += float(p.paid_price)

    total_category = Category.objects.all().count()
    total_product = Product.objects.all().count()
    inventory = Inventory.objects.all()
    total_inventory = inventory.count()
    total_inventory_price = 0
    for i in inventory:
        total_inventory_price += float(i.price)
    total_purchase = 0
    total_purchase_price = 0
    total_sales = 0
    total_sales_price = 0
    total_personnal_cut_price = 0

    personnel_purchase_activities = PurchaseActivity.objects.all()
    for p in personnel_purchase_activities:
        total_purchase += int(p.count)
        total_purchase_price += float(p.count) * float(p.product.price)
    personnel_sales_activities = SaleActivity.objects.all()
    for s in personnel_sales_activities:
        total_sales += int(s.count)
        total_sales_price += float(s.count) * float(s.price)
        total_personnal_cut_price += float(s.count) * float(s.price) * float(s.personnel.cut) / 100.0
    total_personnal_remain_price = (float(total_sales_price) - total_personnal_cut_price) - float(total_personnal_price)
    total_enter_price = total_personnal_cut_price
    total_exit_price = total_inventory_price
    total_diff = total_enter_price - total_exit_price
    return render(request, 'home.html', locals())


@login_required()
def personnel_add(request):
    if request.method == 'POST':
        form = PersonnelAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Üretici Başarıyla Eklendi")
            return redirect('personnel_add')
    else:
        form = PersonnelAddForm()
    personnels = Personnel.objects.all()
    return render(request, 'personnel_add.html', locals())


@login_required()
def personnel_info(request, personnel_code):
    personnel = get_object_or_404(Personnel, id=personnel_code)
    if request.method == 'POST':
        form = PersonnelAddForm(request.POST, request.FILES, instance=personnel)
        if form.is_valid():
            form.save()
            messages.success(request, "Üretici Başarıyla Düzenlendi")
            return redirect('personnel_info', personnel.id)
    else:
        total_purchases = 0
        total_sales = 0
        total_purchases_price = 0
        total_sales_price = 0
        personnel_purchase_activities = PurchaseActivity.objects.filter(personnel=personnel)
        for p in personnel_purchase_activities:
            total_purchases += int(p.count)
            total_purchases_price += float(p.count) * float(p.product.price)
        personnel_sales_activities = SaleActivity.objects.filter(personnel=personnel)
        for s in personnel_sales_activities:
            total_sales += int(s.count)
            total_sales_price += float(s.count) * float(s.price)
        total_remain = total_purchases - total_sales
        total_remain_price = total_purchases_price - total_sales_price
        total_cut = float(total_sales_price) * float(personnel.cut) / 100.0
        total_remain_paid_price = (float(total_sales_price) - total_cut) - float(personnel.paid_price)
        form = PersonnelAddForm(instance=personnel)
    return render(request, 'personnel_info.html', locals())


@login_required()
def personnel_del(request, personnel_code):
    personnel = get_object_or_404(Personnel, id=personnel_code)
    personnel.delete()
    messages.success(request, "Üretici Başarıyla Silindi")
    return redirect('personnel_add')


@login_required()
def category_add(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Üretim Şablonu Başarıyla Eklendi")
            return redirect('category_add')
    else:
        form = CategoryAddForm()
    categories = Category.objects.all()
    return render(request, 'category_add.html', locals())


@login_required()
def category_info(request, category_code):
    category = get_object_or_404(Category, id=category_code)
    if request.method == 'POST':
        form = CategoryAddForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Üretim Şablonu Başarıyla Düzenlendi")
            return redirect('category_info', category.id)
    else:
        form = CategoryAddForm(instance=category)
    return render(request, 'category_info.html', locals())


@login_required()
def category_del(request, category_code):
    category = get_object_or_404(Category, id=category_code)
    category.delete()
    messages.success(request, "Üretim Şablonu Başarıyla Silindi")
    return redirect('category_add')


@login_required()
def product_add(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Üretim Başarıyla Eklendi")
            return redirect('product_add')
    else:
        form = ProductAddForm()
    products = Product.objects.all()
    return render(request, 'product_add.html', locals())


@login_required()
def product_info(request, product_code):
    product = get_object_or_404(Product, id=product_code)
    if request.method == 'POST':
        form = ProductAddForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Üretim Başarıyla Düzenlendi")
            return redirect('product_info', product.id)
    else:
        form = ProductAddForm(instance=product)
    return render(request, 'product_info.html', locals())


@login_required()
def product_del(request, product_code):
    product = get_object_or_404(Product, id=product_code)
    product.delete()
    messages.success(request, "Üretim Başarıyla Silindi")
    return redirect('product_add')


@login_required()
def purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.total = float(p.product.price) * float(p.count)
            p.save()
            messages.success(request, "Alım Kaydı Başarıyla Eklendi")
            return redirect('purchase')
    else:
        form = PurchaseForm()
    purchases = PurchaseActivity.objects.all()
    return render(request, 'purchase.html', locals())


@login_required()
def purchase_info(request, purchase_code):
    purchase = get_object_or_404(PurchaseActivity, id=purchase_code)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            p = form.save(commit=False)
            p.total = float(p.product.price) * float(p.count)
            p.save()
            messages.success(request, "Alım Kaydı Başarıyla Düzenlendi")
            return redirect('purchase_info', purchase.id)
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'purchase_info.html', locals())


@login_required()
def purchase_del(request, purchase_code):
    purchase = get_object_or_404(PurchaseActivity, id=purchase_code)
    purchase.delete()
    messages.success(request, "Alım Kaydı Başarıyla Silindi")
    return redirect('purchase')


@login_required()
def sales(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            if not sale.is_free:
                if float(sale.price) == float(0.0):
                    sale.price = float(sale.product.price) - float(sale.product.price) * float(sale.discount) / 100
                else:
                    sale.discount = 100.0 * (
                        (float(sale.product.price) - float(sale.price)) / float(sale.product.price))
            else:
                sale.price = 0.0
                sale.discount = 100.0
            sale.total = float(sale.product.price) * float(sale.count)
            sale.save()
            messages.success(request, "Satış Kaydı Başarıyla Eklendi")
            return redirect('sales')
    else:
        form = SaleForm()
    sales = SaleActivity.objects.all()
    return render(request, 'sales.html', locals())


@login_required()
def sales_info(request, sale_code):
    sales = get_object_or_404(SaleActivity, id=sale_code)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sales)
        if form.is_valid():
            sale = form.save(commit=False)
            if not sale.is_free:
                if float(sale.price) == float(0.0):
                    sale.price = float(sale.product.price) - float(sale.product.price) * float(sale.discount) / 100
                else:
                    sale.discount = 100.0 * (
                        (float(sale.product.price) - float(sale.price)) / float(sale.product.price))
            else:
                sale.price = 0.0
                sale.discount = 100.0
            sale.total = float(sale.product.price) * float(sale.count)
            sale.save()
            messages.success(request, "Satış Kaydı Başarıyla Düzenlendi")
            return redirect('sales_info', sales.id)
    else:
        form = SaleForm(instance=sales)
    return render(request, 'sales_info.html', locals())


@login_required()
def sales_del(request, sale_code):
    sales = get_object_or_404(SaleActivity, id=sale_code)
    sales.delete()
    messages.success(request, "Satış Kaydı Başarıyla Silindi")
    return redirect('sales')


@login_required()
def inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Envanter Kaydı Başarıyla Eklendi")
            return redirect('inventory')
    else:
        form = InventoryForm()
    inventories = Inventory.objects.all()
    return render(request, 'inventory.html', locals())


@login_required()
def inventory_info(request, inventory_code):
    inventory = get_object_or_404(Inventory, id=inventory_code)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            messages.success(request, "Envanter Kaydı Başarıyla Düzenlendi")
            return redirect('inventory_info', inventory.id)
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'inventory_info.html', locals())


@login_required()
def inventory_del(request, inventory_code):
    inventory = get_object_or_404(Inventory, id=inventory_code)
    inventory.delete()
    messages.success(request, "Envanter Kaydı Başarıyla Silindi")
    return redirect('inventory')


@login_required()
def supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "İşyeri Kaydı Başarıyla Eklendi")
            return redirect('supplier')
    else:
        form = SupplierForm()
    suppliers = Supplier.objects.all()
    return render(request, 'supplier.html', locals())


@login_required()
def supplier_info(request, supplier_code):
    supplier = get_object_or_404(Supplier, id=supplier_code)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, "İşyeri Kaydı Başarıyla Düzenlendi")
            return redirect('supplier_info', supplier.id)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier_info.html', locals())


@login_required()
def supplier_del(request, supplier_code):
    supplier = get_object_or_404(Supplier, id=supplier_code)
    supplier.delete()
    messages.success(request, "İşyeri Kaydı Başarıyla Silindi")
    return redirect('supplier')


def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html')
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            ffield = form.data['username']
            ppasword = form.data['password']
            user = authenticate(username=ffield, password=ppasword)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.add_message(request, messages.ERROR, 'Hesap Kitlenmiş.')
                    return render(request, 'login.html')
            else:
                messages.add_message(request, messages.ERROR, 'Kullanıcı adı veya şifre yanlış.')
                return render(request, 'login.html')
        else:
            messages.add_message(request, messages.ERROR, 'Eksik kullanıcı adı veya şifre.')
            return render(request, 'login.html')


def logout_page(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect('/')
