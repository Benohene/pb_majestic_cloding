from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'
    
    # Code taken from Code Institute Boutique Ado project
    def ready(self):
        import checkout.signals
