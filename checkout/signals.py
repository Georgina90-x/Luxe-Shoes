from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Updates the order total on the lineitem being updated/created. """
    logger.info(f"OrderLineItem saved (created={created}): {instance.id}, \
                updating the order totals.")
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ Updates the order total on the lineitem being deleted. """
    logger.info(f"OrderLineItem with ID {instance.id} was deleted, \
                updating the order totals.")
    instance.order.update_total()
