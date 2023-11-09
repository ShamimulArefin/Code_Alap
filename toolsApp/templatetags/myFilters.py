from django import template

register = template.Library()

@register.filter
def gitCompany(value):
    return value[1:]

@register.filter
def gitDate(value):
    return value[:10]

