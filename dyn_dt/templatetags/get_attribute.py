from django import template
from datetime import datetime

register = template.Library()


@register.filter(name="getattribute")
def getattribute(value, arg):
    try:
        attr_value = getattr(value, arg)
        
        if isinstance(attr_value, datetime):
            return attr_value.strftime("%Y-%m-%d %H:%M:%S")
        
        return attr_value
    except:
        return ''
 

@register.filter
def get(dict_data, key):
    return dict_data.get(key, [])