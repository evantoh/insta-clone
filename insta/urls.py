from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    url('^$',views.user_timelines, name='user_timelines'),
    url(r'^search/',views.search_users, name='search_users'),
    url(r'^profile/(?P<user_id>\d+)/$', views.my_profile, name ='myProfile'),
    url(r'^image/(\d+)',views.single_image,name ='single_photo'),
    url( r'^comment(\d+)', views.comment, name="comment" ),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)