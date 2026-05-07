from django import template

register = template.Library()

@register.filter
def getPercent(numerator,denominator):
    if denominator == 0:
        return "0"
    return f'{(100*(numerator /denominator)):.2f}'