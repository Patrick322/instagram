from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^search/',views.search_results, name = 'search_results'),
    url(r'^accounts/profile/(\d+', views.profile, name = 'profile'),
    url(r'^new/post/', views.new_post, name = 'new-post'),
    url(r'^account/edit-profile/', views.edit_profile, name = 'edit-profile'),    
]

if setting.DEBUG:
    urlpatterns+=static(setting.MEDIA_URL, document_root = setting.MEDIA_ROOT)