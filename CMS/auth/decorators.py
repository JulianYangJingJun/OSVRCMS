# coding=utf-8

from django.http import HttpResponse,Http404,HttpRequest,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.tokens import default_token_generator
from CMS.auth.tokens import default_token_generator

def token_login_required(func):
    def _token_login_required(request, *args, **kwargs):
        try:
            user = User.objects.get(pk=request.GET.get('id'))
        except User.DoesNotExist:
            # return HttpResponse("用户ID出错")
            return HttpResponseRedirect("/error/")
        if default_token_generator.check_token(user, request.GET.get('token'))!=True:
           # return HttpResponse("TOken失效")
            return HttpResponseRedirect("/error/")
        if hasattr(request, 'user'):
            request.user = user
        return func(request, *args, **kwargs)
    return _token_login_required