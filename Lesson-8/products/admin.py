from django.contrib import admin
from .models import Product, Category
from django.template.loader import render_to_string


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=[
        'picture','name', 'category', 
        'cost', 'modified',
        'created'
        # 'test'
    ]

    list_filter = [
        'category', 'modified' , 'created'
    ]

    search_fields = [
        'name', 'description'
    ]

    fieldsets = (
        (
            None, {
                'fields': ('name','category',)
            }
            # 'Default', {
            #     'fields': ('name','category',)
            # }
        ),
        (
            'Content', {
                'fields': ('image','description', 'cost')
            }
        )
    )

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'image':obj.image}
        )
    # def test (self, obj):
    #     return 'test'

class ProductInline (admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'name', 'products_num','modified','created'
    ]
    def products_num(self, obj):
        return obj.product_set.count()

    list_filter = [
            'modified' , 'created'
        ]

    inlines = [
        ProductInline
    ]

    search_fields = ['name']

# Решение без декоратора
# admin.site.register(Product,ProductAdmin)
# admin.site.register(Category, CategoryAdmin)