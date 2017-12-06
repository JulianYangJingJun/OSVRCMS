from ....factory import plugin_factory, plugin_widget_factory

from ....contrib.plugins.dummy.dash_widgets import BaseDummyWidget
# from ....contrib.plugins.image.dash_widgets import BaseImageWidget
from ....contrib.plugins.memo.dash_widgets import (
    BaseMemoWidget,
    BaseTinyMCEMemoWidget,
)
# from ....contrib.plugins.rss_feed.dash_widgets import BaseReadRSSFeedWidget
from ....contrib.plugins.url.dash_plugins import BaseURLPlugin
from ....contrib.plugins.video.dash_widgets import BaseVideoWidget
# from ....contrib.plugins.weather.dash_widgets import BaseWeatherWidget

from .dash_widgets import (
    BaseURLBootstrapThreeBootstrap3DashboardMainWidget,
    BaseBookmarkBootstrapThreeWidget,
    BaseImageBootstrapThreeWidget
)
from .forms import URLBootstrapThreeForm

__title__ = 'dash.contrib.layouts.bootstrap3.dash_plugins'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseURLBootstrapThreePlugin',)

# **************************************************************************
# ****************************** Custom plugins ****************************
# **************************************************************************


class BaseURLBootstrapThreePlugin(BaseURLPlugin):
    """URL dashboard plugin.

    The original `URLPlugin`, as well as the main dash.css, relies on
    presence of wonderful "Font awesome". Although a lot of icon names are
    common between Bootstrap 3 and Font awesome, there are some specific
    icons, that are not present in both. Thus, the original ``URLPlugin`` is
    extended to address those differences.
    """

    form = URLBootstrapThreeForm


sizes = (
    (1, 1),
    # (2, 2),
)

plugin_factory(BaseURLBootstrapThreePlugin,
               'url_bootstrap_three',
               sizes)

# **************************************************************************
# **************************************************************************
# ************************** Registering the widgets ***********************
# **************************************************************************
# **************************************************************************

# **************************************************************************
# ******************* Registering widgets for Dummy plugin *****************
# **************************************************************************


main_sizes = (
    (1, 1),
    (2, 2),
)
plugin_widget_factory(BaseDummyWidget,
                      'bootstrap3_dashboard',
                      'main',
                      'dummy',
                      main_sizes)

# **************************************************************************
# ******************* Registering widgets for Image plugin *****************
# **************************************************************************


main_sizes = (
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 4),
    (5, 5)
)

plugin_widget_factory(BaseImageBootstrapThreeWidget,
                      'bootstrap3_dashboard',
                      'main',
                      'image',
                      main_sizes)

# main_sizes = (
#     (1, 1),
#     (2, 2),
#     (2, 3),
#     (3, 2),
#     (3, 3),
#     (3, 4),
#     (4, 4),
#     (4, 5),
#     (5, 4),
#     (5, 5),
# )
# plugin_widget_factory(BaseImageWidget,
#                       'bootstrap3_dashboard',
#                       'main',
#                       'image',
#                       main_sizes)

# **************************************************************************
# ******************* Registering widgets for Memo plugin ******************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 5),
)
plugin_widget_factory(BaseMemoWidget,
                      'bootstrap3_dashboard',
                      'main',
                      'memo',
                      main_sizes)

# **************************************************************************
# ************** Registering widgets for TinyMCEMemo plugin ****************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 5),
)
plugin_widget_factory(BaseTinyMCEMemoWidget,
                      'bootstrap3_dashboard',
                      'main',
                      'tinymce_memo',
                      main_sizes)

# **************************************************************************
# ******************* Registering the widgets for URL plugin ***************
# **************************************************************************


# Registering URL plugin widgets
main_sizes = (
    (1, 1),
    # (2, 2),
)

plugin_widget_factory(BaseURLBootstrapThreeBootstrap3DashboardMainWidget,
                      'bootstrap3_dashboard',
                      'main',
                      'url_bootstrap_three',
                      main_sizes)

# **************************************************************************
# ***************** Registering the widgets for Video plugin ***************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
plugin_widget_factory(BaseVideoWidget,
                      'bootstrap3_dashboard',
                      'main',
                      'video',
                      main_sizes)

# **************************************************************************
# *************** Registering the widgets for Bookmark plugin ***************
# **************************************************************************

main_sizes = (
    (1, 1),
    # (2, 2),
)
plugin_widget_factory(BaseBookmarkBootstrapThreeWidget,
                      'bootstrap3_dashboard',
                      'main',
                      'bookmark',
                      main_sizes)
