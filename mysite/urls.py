from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
