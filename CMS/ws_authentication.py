# ws_authentication.py
from functools import wraps
from json import loads, dumps

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import exceptions
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token


def _close_reply_channel(message):
    message.reply_channel.send({"close": True})


def authenticate(token):
    """
    Tries to authenticate user based on the supplied token. It also checks
    the token structure and validity.
    """
    try:
        auth_token = Token.objects.get(key=token)
    except Token.DoesNotExist:
        msg = _('Invalid token')
        raise exceptions.AuthenticationFailed(msg)
    """Other authenticate operation"""

    return auth_token.user, auth_token


def ws_auth_request_token(func):
    """
    Checks the presence of a "token" request parameter and tries to
    authenticate the user based on its content.
    The request url must include token.
    eg: /v1/channel/1/?token=abcdefghijklmn
    """
    @wraps(func)
    def inner(message, *args, **kwargs):
        try:
            if "method" not in message.content:
                message.content['method'] = "FAKE"
            request = AsgiRequest(message)
        except Exception as e:
            raise ValueError("Cannot parse HTTP message - are you sure this is a HTTP consumer? %s" % e)

        token = request.GET.get("token", None)

        print request.path,request.GET

        if token is None:
            _close_reply_channel(message)
            raise ValueError("Missing token request parameter. Closing channel.")

        user, token = authenticate(token)

        message.token = token
        message.user = user

        return func(message, *args, **kwargs)
    return inner


def ws_auth_message_token(func):
    """
    Checks the presence of a "token" field on the message's text field and
    tries to authenticate the user based on its content.
    The text must include "token" field.
    eg:{'text':{'token': 'abcdefg','otherdata':''}}.
    """
    @wraps(func)
    def inner(message, *args, **kwargs):
        message_text = message.get('text', None)
        if message_text is None:
            _close_reply_channel(message)
            raise ValueError("Missing text field. Closing channel.")

        try:
            message_text_json = loads(message_text)
        except ValueError:
            _close_reply_channel(message)
            raise

        token = message_text_json.pop('token', None)
        if token is None:
            _close_reply_channel(message)
            raise ValueError("Missing token field. Closing channel.")

        user, token = authenticate(token)

        message.token = token
        message.user = user
        message.text = dumps(message_text_json)

        return func(message, *args, **kwargs)
    return inner