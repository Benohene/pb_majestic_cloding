from django import template

register = template.Library()

'''
This function will calculate the subtotal of the item by multiplying the price by the quantity.
'''
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity