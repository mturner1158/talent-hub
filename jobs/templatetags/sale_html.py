from django import template
from django.utils.safestring import mark_safe

from talenthub.sanitise import clean_html as _clean

register = template.Library()


@register.filter
def clean_html(value):
    return mark_safe(_clean(value))