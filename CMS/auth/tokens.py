from datetime import date,datetime

from django.conf import settings
from django.utils import six
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils.http import base36_to_int, int_to_base36


class PasswordResetTokenGenerator(object):
    """
    Strategy object used to generate and check tokens for the password
    reset mechanism.
    """
    key_salt = "django.contrib.auth.tokens.PasswordResetTokenGenerator"

    def create_user_token(self,user):
        from CMS.models import UserToken
        import datetime
        token = self.make_token(user)
        UserToken.objects.filter(user_id=user.pk).delete()
        UToken = UserToken()
        UToken.user_id = user.pk
        UToken.key = token
        UToken.created_at = user.last_login
        delta = datetime.timedelta(days=settings.PASSWORD_RESET_TIMEOUT_DAYS)
        expire_date = user.last_login + delta
        UToken.expire_date = expire_date.strftime('%Y-%m-%d %H:%M:%S')
        UToken.save()
        return token

    def make_token(self, user):
        """
        Returns a token that can be used once to do a password reset
        for the given user.
        """
        # print (user.pk)


        return self._make_token_with_timestamp(user, self._num_days(self._today()))

    def check_token(self, user, token):
        """
        Check that a password reset token is correct for a given user.
        """
        # Parse the token
        try:
            ts_b36, hash = token.split("-")

        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        if not constant_time_compare(self._make_token_with_timestamp(user, ts), token):

            return False


        if self._num_days(self._today()) - ts > settings.PASSWORD_RESET_TIMEOUT_DAYS:
            return False

        return True

    def _make_token_with_timestamp(self, user, timestamp):
        # timestamp is number of days since 2001-1-1.  Converted to
        # base 36, this gives us a 3 digit string until about 2121
        ts_b36 = int_to_base36(timestamp)
        # print (ts_b36)
        # By hashing on the internal state of the user and using state
        # that is sure to change (the password salt will change as soon as
        # the password is set, at least for current Django auth, and
        # last_login will also change), we produce a hash that will be
        # invalid as soon as it is used.
        # We limit the hash to 20 chars to keep URL short
        # print (self.key_salt)
        hash = salted_hmac(
            self.key_salt,
            self._make_hash_value(user, timestamp),
        ).hexdigest()[::2]
        return "%s-%s" % (ts_b36, hash)

    def _make_hash_value(self, user, timestamp):
        # print (user.last_login)
        # Ensure results are consistent across DB backends
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        # print (login_timestamp)
        return (
            six.text_type(user.pk) + user.password +
            six.text_type(login_timestamp) + six.text_type(timestamp)
        )

    def _num_days(self, dt):
        return (dt - date(2001, 1, 1)).days

    def _today(self):
        # Used for mocking in tests
        return date.today()

default_token_generator = PasswordResetTokenGenerator()
