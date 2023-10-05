'''This file is used to configure the checkout app'''
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    '''This class is used to configure the checkout app'''
    name = "checkout"

    # Code taken from Code Institute Boutique Ado project
    def ready(self):
        import checkout.signals
