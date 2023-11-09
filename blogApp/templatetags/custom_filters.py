from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.filter()
def range_filter(value):
    return value[0:200] + '....'

# register.filter('range_filter', range_filter)

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])