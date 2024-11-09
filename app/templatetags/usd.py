from django import template
register=template.Library()


def swap(value):
    return value.swapcase()

@register.filter('sp')
def splitting(value,arg):
    return value.split(arg)


register.filter('swapping',swap)
#register.filter('splitting',splitting)