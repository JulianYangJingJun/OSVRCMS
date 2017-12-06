# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
# from .models import File
from filer.models import *

register = template.Library()
@register.simple_tag
def GetFileUrl(pk):
    File_Model = File.objects.filter(pk=pk)[:1]
    filter_data = list(File_Model.values('id', 'file', '_file_size', 'sha1', 'uploaded_at'))
    # print THUMBNAIL_ALIASES
    # print (filter_data)
    if settings.USE_TZ:
        canonical_time = int(
            (filter_data[0]['uploaded_at'] - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())
    else:
        canonical_time = int((filter_data[0]['uploaded_at'] - datetime(1970, 1, 1)).total_seconds())
    url = ''
    try:
        url = urlresolvers.reverse('filecanonical', kwargs={
            'uploaded_at': canonical_time,
            'file_id': pk,
        })

        # print (url)
    except urlresolvers.NoReverseMatch:
        pass  # No canonical url, return empty string
    # print settings.URL + url
    return settings.URL + url