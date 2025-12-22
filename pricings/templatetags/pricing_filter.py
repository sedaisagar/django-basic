from django import template


register = template.Library()

@register.filter(name="pub_count")
def pub_count(value):
    return value.features.filter(published=True).count()