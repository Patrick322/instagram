from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.post,name ='post'),
    url(r'^search/',views.search_results, name = 'search_results'),
    url(r'^view/', views.view, name = 'view'),
    url(r'^accounts/profile/(\d+)', views.profile, name = 'profile'),
    url(r'^new/post/', views.new_post, name = 'new-post'),
    url(r'^account/edit-profile/', views.edit_profile, name = 'edit-profile'),    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)