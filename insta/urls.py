from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$',views.user_timelines, name='user_timelines'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/profile/', views.my_profile, name ='myProfile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)