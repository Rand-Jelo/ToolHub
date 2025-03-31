from django.contrib import admin
from .models import Order, OrderItem

# Register OrderItem to display as a related object in the Order admin page
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # How many empty forms to display by default

# Customizing the Order admin interface
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'user__username', 'status')
    inlines = [OrderItemInline]

    # Add custom actions to delete orders
    actions = ['delete_selected_orders']

    def delete_selected_orders(self, request, queryset):
        # Custom delete action to delete selected orders and their items
        for order in queryset:
            # Delete related order items first
            order.items.all().delete()
            order.delete()
        self.message_user(request, f'{queryset.count()} order(s) were successfully deleted.')

    delete_selected_orders.short_description = "Delete selected orders"

# Register the Order model with the admin interface
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)  # Register OrderItem as well