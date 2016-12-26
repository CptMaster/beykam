"""Capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from beykam import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='home'),
    url(r'^giris/$', views.login_page, name='login'),
    url(r'^cikis/$', views.logout_page, name='logout'),
    url(r'^uretici-kayit-alani/$', views.personnel_add, name='personnel_add'),
    url(r'^uretici/(?P<personnel_code>\d+)/$', views.personnel_info, name='personnel_info'),
    url(r'^uretici/del/(?P<personnel_code>\d+)/$', views.personnel_del, name='personnel_del'),
    url(r'^uretim-sablon-ekle/$', views.category_add, name='category_add'),
    url(r'^sablon/(?P<category_code>\d+)/$', views.category_info, name='category_info'),
    url(r'^sablon/del/(?P<category_code>\d+)/$', views.category_del, name='category_del'),
    url(r'^uretim-kayit-alani', views.product_add, name='product_add'),
    url(r'^uretim/(?P<product_code>\d+)/$', views.product_info, name='product_info'),
    url(r'^uretim/del/(?P<product_code>\d+)/$', views.product_del, name='product_del'),
    url(r'^alim/$', views.purchase, name='purchase'),
    url(r'^alim/(?P<purchase_code>\d+)/$', views.purchase_info, name='purchase_info'),
    url(r'^alim/del/(?P<purchase_code>\d+)/$', views.purchase_del, name='purchase_del'),
    url(r'^satis/$', views.sales, name='sales'),
    url(r'^satis/(?P<sale_code>\d+)/$', views.sales_info, name='sales_info'),
    url(r'^satis/del/(?P<sale_code>\d+)/$', views.sales_del, name='sales_del'),
    url(r'^envanter/$', views.inventory, name='inventory'),
    url(r'^envanter/(?P<inventory_code>\d+)/$', views.inventory_info, name='inventory_info'),
    url(r'^envanter/del/(?P<inventory_code>\d+)/$', views.inventory_del, name='inventory_del'),
    url(r'^is-yerleri/$', views.supplier, name='supplier'),
    url(r'^isyeri/(?P<supplier_code>\d+)/$', views.supplier_info, name='supplier_info'),
    url(r'^isyeri/del/(?P<supplier_code>\d+)/$', views.supplier_del, name='supplier_del'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)