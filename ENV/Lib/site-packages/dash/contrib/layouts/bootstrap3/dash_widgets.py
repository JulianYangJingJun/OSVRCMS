from ....contrib.plugins.image.dash_widgets import BaseImageWidget
from ....contrib.plugins.url.dash_widgets import (
    BaseBookmarkWidget,
    BaseURLWidget,
)

__title__ = 'dash.contrib.layouts.bootstrap3.dash_widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseBookmarkBootstrapThreeWidget',
    'BaseImageBootstrapThreeWidget',
    'BaseURLBootstrapThreeBootstrap3DashboardMainWidget',
)

# *************************************************************
# ******************* URL widgets *****************************
# *************************************************************


class BaseURLBootstrapThreeBootstrap3DashboardMainWidget(BaseURLWidget):
    """Base URL plugin widget for Bootstrap 3 Fluid layout.

    Placeholder `main` widget.
    """

    # layout_uid = 'bootstrap3_fluid'
    # placeholder_uid = 'main'
    # plugin_uid = 'url_bootstrap_three'
    media_css = (
        'bootstrap3/css/dash_plugin_url_bootstrap3.css',
    )

# *********************************************************
# *********************************************************
# *********************** Bookmark widgets ****************
# *********************************************************
# *********************************************************


class BaseBookmarkBootstrapThreeWidget(BaseBookmarkWidget):
    """Base Bookmark plugin widget for Bootstrap 3 Dashboard layout."""

    media_css = (
        'bootstrap3/css/dash_plugin_bookmark_bootstrap3.css',
    )

# *********************************************************
# *********************************************************
# *********************** Image widgets *******************
# *********************************************************
# *********************************************************


class BaseImageBootstrapThreeWidget(BaseImageWidget):
    """Base Image plugin widget for Bootstrap 3 Dashboard layout."""

    media_js = (
        'bootstrap3/js/dash_plugin_image_bootstrap3.js',
    )
