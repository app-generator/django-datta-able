import requests, base64, json, csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe
from django.conf import settings
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.views import View
from django.db import models
from pprint import pp 

from apps.dyn_dt.models import ModelFilter, PageItems, HideShowFilter
from apps.dyn_dt.utils import user_filter

from cli import *

# Create your views here.

def index(request):
    
    context = {
        'routes' : settings.DYNAMIC_DATATB.keys()
    }

    return render(request, 'dyn_dt/index.html', context)

def create_filter(request, model_name):
    model_name = model_name.lower()
    if request.method == "POST":
        keys = request.POST.getlist('key')
        values = request.POST.getlist('value')
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]

            ModelFilter.objects.update_or_create(
                parent=model_name,
                key=key,
                defaults={'value': value}
            )

        return redirect(reverse('model_dt', args=[model_name]))


def create_page_items(request, model_name):
    model_name = model_name.lower()
    if request.method == 'POST':
        items = request.POST.get('items')
        page_items, created = PageItems.objects.update_or_create(
            parent=model_name,
            defaults={'items_per_page':items}
        )
        return redirect(reverse('model_dt', args=[model_name]))


def create_hide_show_filter(request, model_name):
    model_name = model_name.lower()
    if request.method == "POST":
        data_str = list(request.POST.keys())[0]
        data = json.loads(data_str)

        HideShowFilter.objects.update_or_create(
            parent=model_name,
            key=data.get('key'),
            defaults={'value': data.get('value')}
        )

        response_data = {'message': 'Model updated successfully'}
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def delete_filter(request, model_name, id):
    model_name = model_name.lower()
    filter_instance = ModelFilter.objects.get(id=id, parent=model_name)
    filter_instance.delete()
    return redirect(reverse('model_dt', args=[model_name]))


def get_model_field_names(model, field_type):
    """Returns a list of field names based on the given field type."""
    return [
        field.name for field in model._meta.get_fields() 
        if isinstance(field, field_type)
    ]

def model_dt(request, aPath):
    aModelName  = None
    aModelClass = None
    choices_dict = {}

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )
    
    #db_fields = [field.name for field in aModelClass._meta.get_fields() if not field.is_relation]
    db_fields = [field.name for field in aModelClass._meta.fields]
    fk_fields = get_model_fk_values(aModelClass)
    db_filters = []
    for f in db_fields:
        if f not in fk_fields.keys():
            db_filters.append( f )

    for field in aModelClass._meta.fields:
        if field.choices:
            choices_dict[field.name] = field.choices

    field_names = []
    for field_name in db_fields:
        fields, created = HideShowFilter.objects.get_or_create(key=field_name, parent=aPath.lower())
        if fields.key in db_fields:
            field_names.append(fields)
    
    model_series = {}
    for f in db_fields:
        f_values = list ( aModelClass.objects.values_list( f, flat=True) )
        model_series[ f ] = ', '.join( str(i) for i in f_values)

    # model filter
    filter_string = {}
    filter_instance = ModelFilter.objects.filter(parent=aPath.lower())
    for filter_data in filter_instance:
        if filter_data.key in db_fields: 
            filter_string[f'{filter_data.key}__icontains'] = filter_data.value

    order_by = request.GET.get('order_by', 'id')
    if order_by not in db_fields:
        order_by = 'id'
    
    queryset = aModelClass.objects.filter(**filter_string).order_by(order_by)
    item_list = user_filter(request, queryset, db_fields, fk_fields.keys())

    # pagination
    page_items = PageItems.objects.filter(parent=aPath.lower()).last()
    p_items = 25
    if page_items:
        p_items = page_items.items_per_page

    page = request.GET.get('page', 1)
    paginator = Paginator(item_list, p_items)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        return redirect(reverse('model_dt', args=[aPath]))
    except EmptyPage:
        return redirect(reverse('model_dt', args=[aPath]))
    
    read_only_fields = ('id', )

    integer_fields = get_model_field_names(aModelClass, models.IntegerField)
    date_time_fields = get_model_field_names(aModelClass, models.DateTimeField)
    email_fields = get_model_field_names(aModelClass, models.EmailField)
    text_fields = get_model_field_names(aModelClass, (models.TextField, models.CharField))
    
    context = {
        'page_title': 'Dynamic DataTable - ' + aPath.lower().title(),
        'link': aPath,
        'field_names': field_names,
        'db_field_names': db_fields,
        'db_filters': db_filters,
        'items': items,
        'page_items': p_items,
        'filter_instance': filter_instance,
        'read_only_fields': read_only_fields,

        'integer_fields': integer_fields,
        'date_time_fields': date_time_fields,
        'email_fields': email_fields,
        'text_fields': text_fields,
        'fk_fields_keys': list( fk_fields.keys() ),
        'fk_fields': fk_fields ,
        'choices_dict': choices_dict,
    }
    return render(request, 'dyn_dt/model.html', context)


@login_required(login_url='/accounts/login/')
def create(request, aPath):
    aModelClass = None

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )

    if request.method == 'POST':
        data = {}
        fk_fields = get_model_fk(aModelClass)

        for attribute, value in request.POST.items():
            if attribute == 'csrfmiddlewaretoken':
                continue

            # Process FKs    
            if attribute in fk_fields.keys():
                value = name_to_class( fk_fields[attribute] ).objects.filter(id=value).first()
            
            data[attribute] = value if value else ''

        aModelClass.objects.create(**data)

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/login/')
def delete(request, aPath, id):
    aModelClass = None

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )
    
    item = aModelClass.objects.get(id=id)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/login/')
def update(request, aPath, id):
    aModelClass = None

    if aPath in settings.DYNAMIC_DATATB.keys():
        aModelName  = settings.DYNAMIC_DATATB[aPath]
        aModelClass = name_to_class(aModelName)

    if not aModelClass:
        return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )

    item = aModelClass.objects.get(id=id)
    fk_fields = get_model_fk(aModelClass)

    if request.method == 'POST':
        for attribute, value in request.POST.items():

            if attribute == 'csrfmiddlewaretoken':
                continue

            if getattr(item, attribute, value) is not None:

                # Process FKs    
                if attribute in fk_fields.keys():
                    value = name_to_class( fk_fields[attribute] ).objects.filter(id=value).first()

                setattr(item, attribute, value)
        
        item.save()

    return redirect(request.META.get('HTTP_REFERER'))



# Export as CSV
class ExportCSVView(View):
    def get(self, request, aPath):
        aModelName  = None
        aModelClass = None

        if aPath in settings.DYNAMIC_DATATB.keys():
            aModelName  = settings.DYNAMIC_DATATB[aPath]
            aModelClass = name_to_class(aModelName)

        if not aModelClass:
            return HttpResponse( ' > ERR: Getting ModelClass for path: ' + aPath )
        
        db_field_names = [field.name for field in aModelClass._meta.get_fields()]
        fields = []
        show_fields = HideShowFilter.objects.filter(value=False, parent=aPath.lower())
        
        for field in show_fields:
            if field.key in db_field_names:
                fields.append(field.key)
            else:
                print(f"Field {field.key} does not exist in {aModelClass} model.")

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{aPath.lower()}.csv"'

        writer = csv.writer(response)
        writer.writerow(fields)  # Write the header

        filter_string = {}
        filter_instance = ModelFilter.objects.filter(parent=aPath.lower())
        for filter_data in filter_instance:
            filter_string[f'{filter_data.key}__icontains'] = filter_data.value

        order_by = request.GET.get('order_by', 'id')
        queryset = aModelClass.objects.filter(**filter_string).order_by(order_by)

        items = user_filter(request, queryset, db_field_names)

        for item in items:
            row_data = []
            for field in fields:
                try:
                    row_data.append(getattr(item, field))
                except AttributeError:
                    row_data.append('') 
            writer.writerow(row_data)

        return response