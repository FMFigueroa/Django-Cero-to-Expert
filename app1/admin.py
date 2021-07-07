from django.contrib import admin
from .models import Category , Producto , Contacto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "category", "precio", "disponible")
    list_editable = ("precio",)
    search_fields = ("nombre",)
    list_filter = ("category","disponible")
    #list_per_page = 1
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = 'Default Category'
    actions = ('change_category_to_default',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)