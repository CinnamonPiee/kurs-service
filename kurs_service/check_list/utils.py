# Вспомогательные функции для работы с корзиной в сессии
from .models import CheckListOrderItem


def get_session_cart(request):
    return request.session.get("check_list", {})


def save_session_cart(request, cart):
    request.session["check_list"] = cart
    request.session.modified = True


def add_to_cart(request, service_id, service_name, img_url):
    cart = get_session_cart(request)
    if str(service_id) in cart:
        cart[str(service_id)]["quantity"] += 1
    else:
        cart[str(service_id)] = {
            "service_id": service_id,
            "service_name": service_name,
            "img_url": img_url,
            "quantity": 1,
        }
    save_session_cart(request, cart)


def increment_cart_item(request, service_id):
    cart = get_session_cart(request)
    if str(service_id) in cart:
        cart[str(service_id)]["quantity"] += 1
        save_session_cart(request, cart)


def decrement_cart_item(request, service_id):
    cart = get_session_cart(request)
    if str(service_id) in cart:
        cart[str(service_id)]["quantity"] -= 1
        if cart[str(service_id)]["quantity"] <= 0:
            del cart[str(service_id)]
        save_session_cart(request, cart)


def remove_cart_item(request, service_id):
    cart = get_session_cart(request)
    if str(service_id) in cart:
        del cart[str(service_id)]
        save_session_cart(request, cart)


def get_cart_items(request):
    cart = get_session_cart(request)
    return [v for v in cart.values()]


def get_cart_count(request):
    cart = get_session_cart(request)
    return sum(item["quantity"] for item in cart.values())
