from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Display these fields in the list view of the admin panel
    list_display = ('id', 'name', 'category', 'price', 'distance', 'difficulty', 'terrain', 'elevation', 'order_id')
    # Allow search functionality on these fields
    search_fields = ('name', 'category', 'distance', 'difficulty', 'terrain', 'elevation')
    # Enable filtering options in the admin panel
    list_filter = ('category', 'difficulty', 'terrain', 'elevation')

# Register the Product model with this custom admin configuration
admin.site.register(Product, ProductAdmin)
