from django.contrib import admin
from FurnitureApp.models import FurnitureShop,Furniturelist
# Register your models here.

# class AdminProduct(admin.ModelAdmin):
#     list_display = ['pname', 'price', 'category']



# class AdminCategory(admin.ModelAdmin):
#     list_display = ['name']

admin.site.register(FurnitureShop)
admin.site.register(Furniturelist)
# admin.site.register(Product,AdminProduct)
# admin.site.register(Category,AdminCategory)

