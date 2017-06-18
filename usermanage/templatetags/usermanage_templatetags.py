from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def prepend_dollars(dollars):
    if dollars:
        dollars = round(float(dollars), 2)
        return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
    else:
        return "$%s" % ("%0.2f" % dollars)
