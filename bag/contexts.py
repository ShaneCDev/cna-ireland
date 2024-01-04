from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    discount_applied = False
    bag = request.session.get('bag', {})
    discount_price = 0

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        if item_data >= 5:
            discount_applied = True

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    if discount_applied:
        discount_price = (grand_total * 10) / 100 
        grand_total = grand_total - discount_price

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount_applied': discount_applied,
        'discount_amount': discount_price,
        'grand_total': grand_total,
    }

    return context
