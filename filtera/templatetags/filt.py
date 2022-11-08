from django import template
register=template.Library()

def truncate(value):
    result=value[0:5]
    return result

def trunket_n(value,n):
    result=value[0:n]
    return result


register.filter("truncate",truncate)
register.filter("trunket_n",trunket_n)