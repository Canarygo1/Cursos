
from django.conf.url import url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^about/$',),
    url(r'^$',)
]
