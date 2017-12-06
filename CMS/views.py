# coding=utf-8

from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404, redirect,render
from .models import File
from django import forms
from django.contrib.auth.decorators import login_required
from .auth.decorators import token_login_required
from CMS.models import Ad,Video,Game,Image,VideoGenres,ImageGenres
from datetime import date
from django.utils import six
# from django.views.decorators.cache import cache_page, cache_control, never_cache

# @token_login_required
# @cache_page(60 * 15, key_prefix="osvr")
def index(request):
    JXAd = Ad.objects.all().filter(local=1)
    YSJx = Video.objects.all().order_by('sorting').filter(is_recommend=1)[:8]
    YXJx =  Game.objects.all().order_by('sorting').filter(is_recommend=1)[:8]
    TPJx = Image.objects.all().order_by('sorting').filter(is_recommend=1)[:6]
    return render(request, 'CMS/index.html',
                  {'JXAd':list(JXAd),
                   'YSJx':list(YSJx),
                   'YXJx':list(YXJx),
                   'TPJx':list(TPJx),
                   })


# @cache_page(60 * 15, key_prefix="osvr")
def video(request):
    Genres       = VideoGenres.objects.all().order_by('created_at')
    Video_data   = Video.objects.filter(is_recommend=1).order_by('sorting')[:3]
    return render(request, 'CMS/video.html',
                  {'Genres':list(Genres),
                   'Video':list(Video_data),
                   })
# @cache_page(60 * 15, key_prefix="osvr")
def image(request):
    Image_Genres = ImageGenres.objects.all().order_by('created_at')
    Image_Date   = Image.objects.filter(is_recommend=1).order_by('sorting')[:5]
    # for N in Image_Date:
    #     print N['id']
    # print Image_Date.values_list('imageurl_id')
    # #
    # # filer_file = get_object_or_404(File, pk=ImageSerializer.imageurl_id, is_public=True)
    # # from easy_thumbnails.files import get_thumbnailer
    # # thumb_url = get_thumbnailer(filer_file)['imagecover'].url
    #
    #

    return render(request, 'CMS/image.html',
                  {'ImageGenres':list(Image_Genres),
                   'Image':list(Image_Date),
                   })

# @cache_page(60 * 15, key_prefix="osvr")
def game(request):
    return render(request, 'CMS/game.html')

@token_login_required
def UserCenter(request):
    return HttpResponse('这里是用户中心')


def live(request):
    return render(request, 'CMS/live.html')

# @cache_page(60 * 15, key_prefix="osvr")
def error(request):
    string = "ddd"
    return render(request,'CMS/alert.html',{'string':string})




def filecanonical(request, uploaded_at, file_id,THUMBNAIL_ALIASES=None):

    # """
    # Redirect to the current url of a public file
    # """
    filer_file = get_object_or_404(File, pk=file_id, is_public=True)
    if (not filer_file.file or int(uploaded_at) != filer_file.canonical_time):
        raise Http404('No %s matches the given query.' % File._meta.object_name)

    # if filer_file.file_type=="Image" and THUMBNAIL_ALIASES!=None:
    #     from easy_thumbnails.files import get_thumbnailer
    #     thumb_url = get_thumbnailer(filer_file)[THUMBNAIL_ALIASES].url
    #     return redirect(thumb_url)

    return redirect(filer_file.url)




# def _num_days(self, dt):
#     return (date.today() - date(2001, 1, 1)).days
#
# def _today(self):
#     # Used for mocking in tests
#     return date.today()
# def int_to_base36(i):
#     """
#     Converts an integer to a base36 string
#     """
#     char_set = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if i < 0:
#         raise ValueError("Negative base36 conversion input.")
#     if six.PY2:
#         if not isinstance(i, six.integer_types):
#             raise TypeError("Non-integer base36 conversion input.")
#         if i > sys.maxint:
#             raise ValueError("Base36 conversion input too large.")
#     if i < 36:
#         return char_set[i]
#     b36 = ''
#     while i != 0:
#         i, n = divmod(i, 36)
#         b36 = char_set[n] + b36
#     return b36

# @token_login_required
# def abc(request):
#     return HttpResponse(request.user)





# def create_captcha(request):
#     from captcha.models import CaptchaStore
#     from captcha.helpers import captcha_image_url
#     try:
#         import json
#     except ImportError:
#         from django.utils import simplejson as json
#
#     new_key = CaptchaStore.pick()
#     to_json_response = {
#         'key': new_key,
#         'image_url': captcha_image_url(new_key),
#     }
#     return HttpResponse(json.dumps(to_json_response), content_type='application/json')

    # return HttpResponse(captcha_image_url(new_key))


from django.http import FileResponse
def file_down(request):
    file=open(r'http://127.0.0.7:8000//media//filer_public//ac//a4//aca43624-f1ac-428d-b2ad-e1494f620ae4//3d_chef.mov','wb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="3d_chef.mov"'
    return response









