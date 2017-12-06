from django.conf.urls import url,include
from django.http import HttpResponse
from CMS import views

urlpatterns = [
    # url(r'^$',views.index),
    url(r'^index/', views.index),
    url(r'^video/', views.video),
    url(r'^image/', views.image),
    url(r'^game/', views.game),
    url(r'^live/', views.live),
    url(r'^User/', views.UserCenter),
    url(r'^error/', views.error),

    url(r'^d/',views.file_down),
    # url(r'^GetGenresVideo/',views.GetGenresVideo),
    # url(r'^abc/',views.abc),
    url(r'(?P<uploaded_at>[0-9]+)/(?P<file_id>[0-9]+)/$',
            views.filecanonical,
            name='filecanonical'
    ),
]