from django.db.models import Q

def user_filter(request, queryset, fields, fk_fields=[]):
    value = request.GET.get('search')
    
    if value:
        dynamic_q = Q()
        for field in fields:
            if field not in fk_fields:
                dynamic_q |= Q(**{f'{field}__icontains': value})
        return queryset.filter(dynamic_q)

    return queryset