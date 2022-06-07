from django import template
from f1data.models import Result, Season

register = template.Library()

@register.filter(name='constructor')
def constructor(value,season):
    return season.results.filter(driver=value.driver).first().constructor.name
