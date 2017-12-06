from django.utils.translation import ugettext_lazy as _

__title__ = 'dash.contrib.layouts.bootstrap3.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'IMAGE_CHOICES',
    'IMAGE_CHOICES_WITH_EMPTY_OPTION',
)


IMAGE_CHOICES = (
    # Icons that are also present in `URLPlugin`.
    ('glyphicon-film', _("Film")),
    # ('glyphicon-coffee', _("Coffee")),
    ('glyphicon-calendar', _("Calendar")),
    ('glyphicon-book', _("Book")),
    ('glyphicon-music', _("Music")),
    ('glyphicon-picture', _("Picture")),
    # ('glyphicon-rss-sign', _("RSS")),
    ('glyphicon-star', _("Star")),
    ('glyphicon-thumbs-up', _("Thumbs-up")),
    # ('glyphicon-smile', _("Smile")),
    # ('glyphicon-gamepad', _("Gamepad")),
    ('glyphicon-plane', _("Plane")),
    ('glyphicon-road', _("Road")),
    ('glyphicon-camera', _("Camera")),
    ('glyphicon-download', _("Download")),
    # ('glyphicon-food', _("Food")),
    ('glyphicon-info-sign', _("Info")),
    ('glyphicon-shopping-cart', _("Shopping cart")),
    # ('glyphicon-truck', _("Truck")),
    ('glyphicon-wrench', _("Wrench")),
    # ('glyphicon-facebook', _("Facebook")),
    # ('glyphicon-github', _("Github")),
    # ('glyphicon-google-plus', _("Google plus")),
    # ('glyphicon-linkedin', _("LinkedIn")),
    # ('glyphicon-pinterest', _("Pinterest")),
    # ('glyphicon-twitter', _("Twitter")),
    # ('glyphicon-youtube', _("Youtube")),
    # ('glyphicon-bitbucket', _("Bitbucket")),
    # ('glyphicon-android', _("Android")),
    # ('glyphicon-apple', _("Apple")),
    # ('glyphicon-windows', _("Windows")),
    # ('glyphicon-tumblr-sign', _("Tumblr")),
    # ('glyphicon-instagram', _("Instagram")),
    # ('glyphicon-dropbox', _("Dropbox")),
    # ('glyphicon-trophy', _("Trophy")),
    # ('glyphicon-legal', _("Legal")),
    ('glyphicon-lock', _("Lock")),
    ('glyphicon-heart', _("Heart")),
    ('glyphicon-question-sign', _("Question")),
    ('glyphicon-headphones', _("Headphones")),
    ('glyphicon-gift', _("Gift")),
    # ('glyphicon-key', _("Key")),
    # ('glyphicon-female', _("Female")),
    # ('glyphicon-male', _("Male")),
    ('glyphicon-comment', _("Comment")),
    # ('glyphicon-bug', _("Bug")),
    ('glyphicon-bell', _("Bell")),
    ('glyphicon-search', _("Search")),
    ('glyphicon-map-marker', _("Map marker")),
    ('glyphicon-globe', _("Globe")),
    ('glyphicon-pencil', _("Pensil")),
    ('glyphicon-tasks', _("Tasks")),
)

IMAGE_CHOICES_WITH_EMPTY_OPTION = [('', '---------')] + list(IMAGE_CHOICES)
