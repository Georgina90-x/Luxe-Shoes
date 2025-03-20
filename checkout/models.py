import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile
from decimal import Decimal


class Promo(models.Model):
    promocode = models.CharField(max_length=50)
    discount = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.promocode


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label="Select Your Country*", null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    # promos = models.ManyToManyField(Promo, blank=True)
    vat_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254,
                                  null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generates a random set of numbers to represent the order number.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates the grand total when a new line is added. Inc delivery price.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum('lineitem_total'))
            ['lineitem_total__sum'] or 0
        )
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PRICE / 100
            )
        else:
            self.delivery_cost = 0

        vat_calc = Decimal(settings.VAT_CALC)
        self.vat_total = (self.order_total * vat_calc).quantize(Decimal('0.01'))

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Generates order number if not set. """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=10, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=20,
                                         decimal_places=2, null=True,
                                         blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides original save method and updates the order/line item total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Item Number: {self.product.sku} on order {self.order.order_number}'
