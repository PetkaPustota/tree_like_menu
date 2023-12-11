from django import template
from django.db.models import Prefetch, Value, Window, F, IntegerField, When, Case, Sum
from django.db.models.functions import Lead, Lag

from menu.models import *

register = template.Library()
menu_dict = Menu.get_tree_as_dict()


def wrapper(filter, menu_items):
    if menu_items is None:
        menu_items = []
        menu_items.append(menu_dict.get(filter))
    return {"menu_items": menu_items, "name": filter}


# template tag для вывода меню в шаблоны
@register.inclusion_tag('test.html')
def draw_menu(filter, menu_items=None):
    return wrapper(filter, menu_items)
