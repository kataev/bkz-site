from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.middleware.common import CommonMiddleware

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',include(admin.site.urls)),
    url(r'^tinymce/',include('tinymce.urls')),

    url(r'^$', 'bkz.views.main'),
#    url(r'^about/$', 'bkz.views.about'),
)


urlpatterns+= staticfiles_urlpatterns()