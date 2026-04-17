from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Access dict by key in templates: {{ my_dict|get_item:some_var }}"""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None


@register.filter
def paper_label(value):
    """Convert 'paper1' -> 'Paper 1', 'paper2' -> 'Paper 2'."""
    return value.replace('paper', 'Paper ').replace('mixed', 'Mixed') if value else value


@register.filter
def percentage(value, total):
    """Return integer percentage: {{ done|percentage:total }}"""
    try:
        return int(int(value) / int(total) * 100)
    except (ValueError, ZeroDivisionError, TypeError):
        return 0


@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)
