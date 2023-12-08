from django.contrib import admin
from .models import Category, Product, ProductReview

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'stars',
        'review_date', 
        'product'
    )

    ordering = ('created_on',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)