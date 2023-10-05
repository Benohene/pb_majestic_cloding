'''Signals for checkout app'''
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# Code taken from Code Institute Boutique Ado project


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    '''Update order total on lineitem update/create
    Code taken from Code Institute Boutique Ado project
    '''
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    '''Update order total on lineitem delete
    Code taken from Code Institute Boutique Ado project
    '''
    instance.order.update_total()
