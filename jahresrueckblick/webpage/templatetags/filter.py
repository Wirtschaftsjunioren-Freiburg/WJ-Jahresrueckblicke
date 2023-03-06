from django import template

register = template.Library()

@register.filter
def getChairmen(value):
    return value.filter(chairman=True)

@register.filter
def getNonChairmen(value):
    return value.filter(chairman=False)