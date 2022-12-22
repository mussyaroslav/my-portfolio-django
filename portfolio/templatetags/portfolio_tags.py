from django import template

from portfolio.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()
