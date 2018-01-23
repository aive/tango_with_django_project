from django.conf.urls import url
from rango import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
]

# the previous command is appending a call to the static() function
# to your project’s urlpatterns list.

# also added 2 import commands at top, for settings and static
# Once this is complete, you should be able to serve content from
# the media directory of your project from the /media/ URL.


# MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# MEDIA_ROOT = MEDIA_DIR
# MEDIA_URL = '/media/'