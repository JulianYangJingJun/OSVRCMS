try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'dash.contrib.layouts.bootstrap3'
        label = 'dash_contrib_layouts_bootstrap3'

except ImportError:
    pass

__title__ = 'dash.contrib.layouts.bootstrap3.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)
