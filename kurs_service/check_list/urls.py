from django.urls import path
from . import views


app_name = "check_list"


urlpatterns = [
    path("", views.check_list, name="check_list"),
    path("count/", views.check_list_count, name="check_list_count"),
    path("index/", views.check_list_index, name="check_list_index"),
    path("add/", views.add_to_check_list, name="add_to_check_list"),
    path("increment/", views.increment_check_list, name="increment_check_list"),
    path("decrement/", views.decrement_check_list, name="decrement_check_list"),
    path("del-item/", views.remove_check_list_item, name="remove_check_list_item"),
]
