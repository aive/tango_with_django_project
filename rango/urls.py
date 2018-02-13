from django.conf.urls import url
from rango import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'), # New pattern!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]

    # the previous command is appending a call to the static() function
    # to your project’s urlpatterns list.

    # also added 2 import commands at top, for settings and static
    # Once this is complete, you should be able to serve content from
    # the media directory of your project from the /media/ URL.

    # MEDIA_DIR = os.path.join(BASE_DIR, 'media')

    # MEDIA_ROOT = MEDIA_DIR
    # MEDIA_URL = '/media/'
