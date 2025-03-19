from django.contrib import admin
from .models import Order, OrderLineItem, Promo


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'street_address1',
              'street_address2', 'town_or_city', 'county',
              'postcode', 'country', 'phone_number',
              'delivery_cost', 'promos', 'order_total',
              'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'full_name', 'email',
                    'delivery_cost',
                    'order_total', 'grand_total',)

    filter_horizontal = ('promos',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Promo)  # register code for Promo Code in Checkout
