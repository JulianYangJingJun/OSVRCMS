# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
# from .models import File
from filer.models import *
from django.shortcuts import get_object_or_404, redirect,render

register = template.Library()
@register.simple_tag
def GetFileImageAliases(pk,THUMBNAIL_ALIASES):
    try:
        filer_file = get_object_or_404(File, pk=pk, is_public=True)
        from easy_thumbnails.files import get_thumbnailer
        thumb_url = get_thumbnailer(filer_file)[THUMBNAIL_ALIASES].url
    except:
        return settings.URL

    return settings.URL+thumb_url
