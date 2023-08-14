from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    
    # Code taken from Code Institute Boutique Ado project
    def ready(self):
        import checkout.signals
