from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# the previous command is appending a call to the static() function
# to your project’s urlpatterns list.

# also added 2 import commands at top, for settings and static
# Once this is complete, you should be able to serve content from
# the media directory of your project from the /media/ URL.

