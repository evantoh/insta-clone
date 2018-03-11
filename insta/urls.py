from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    url('^$',views.index, name='index'),
    url(r'^search/',views.search_users, name='search_users'),
    url(r'^profile/(?P<id>\d+)/$', views.profile, name ='myProfile'),
    url(r'^image/(\d+)',views.single_image,name ='single_photo'),
    url(r'^comments/(?P<pk>\d+)',views.post_comment, name='comment'),
    url('^upload/',views.upload, name='upload'),
    url(r'^insta_users/$', views.other_insta_users, name='otherinstausers'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)