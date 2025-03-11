from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Updates the order total on the lineitem being updated/created. """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, *args, **kwargs):
    """ Updates the order total on the lineitem being deleted. """
    instance.order.update_total()
