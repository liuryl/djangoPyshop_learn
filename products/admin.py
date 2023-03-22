from django.contrib import admin

# Register your models here.


from .models import Product,Offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
# 添加模块
admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
