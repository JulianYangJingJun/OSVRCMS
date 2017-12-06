from ....base import (
    BaseDashboardLayout,
    BaseDashboardPlaceholder,
    layout_registry
)

__title__ = 'dash.contrib.layouts.bootstrap3.dash_layouts'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Bootstrap3FluidLayout',)


# *******************************************************************
# ******************** Bootstrap 3 Fluid layout *********************
# *******************************************************************

class Bootstrap3FluidMainPlaceholder(BaseDashboardPlaceholder):
    """Main placeholder."""

    uid = 'main'
    cols = 10
    rows = 9
    cell_width = 70
    cell_height = 40
    cell_margin_top = 8
    cell_margin_right = 8
    cell_margin_bottom = 8
    cell_margin_left = 8
    edit_template_name = 'bootstrap3/dashboard_base_placeholder_edit.html'


class Bootstrap3FluidLayout(BaseDashboardLayout):
    """Bootstrap 3 Dashboard layout."""

    uid = 'bootstrap3_dashboard'
    name = 'Bootstrap 3 Dashboard'
    view_template_name = 'bootstrap3/dashboard_view_layout.html'
    edit_template_name = 'bootstrap3/dashboard_edit_layout.html'
    plugin_widgets_template_name_ajax = 'bootstrap3/plugin_widgets_ajax.html'
    form_snippet_template_name = \
        'bootstrap3/snippets/generic_form_snippet.html'
    add_dashboard_entry_ajax_template_name = \
        'bootstrap3/add_dashboard_entry_ajax.html'
    edit_dashboard_entry_ajax_template_name = \
        'bootstrap3/edit_dashboard_entry_ajax.html'

    # create_dashboard_workspace_template_name = \
    #     'bootstrap3/create_dashboard_workspace.html'
    create_dashboard_workspace_ajax_template_name = \
        'bootstrap3/create_dashboard_workspace_ajax.html'
    # edit_dashboard_workspace_template_name = \
    #     'bootstrap3/edit_dashboard_workspace.html'
    edit_dashboard_workspace_ajax_template_name = \
        'bootstrap3/edit_dashboard_workspace_ajax.html'

    placeholders = [Bootstrap3FluidMainPlaceholder]
    cell_units = 'px'
    media_css = (
        'bootstrap3/css/bootstrap.min.css',
        'bootstrap3/css/dashboard.css',
        'bootstrap3/css/dash_layout_bootstap3_dashboard.css',
        # 'css/dash_solid_borders.css',
    )
    media_js = (
        'bootstrap3/js/bootstrap.min.js',
        'bootstrap3/js/dash_layout_bootstap3_dashboard.js',
    )

    def get_view_template_name(self, request=None, origin=None):
        """Override the master view template for public dashboard app."""
        if origin == 'dash.public_dashboard':
            return 'bootstrap3/dashboard_public_dashboard_view_layout.html'
        else:
            return super(Bootstrap3FluidLayout, self).get_view_template_name(
                request=request,
                origin=origin
            )


layout_registry.register(Bootstrap3FluidLayout)
