from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.middleware.common import CommonMiddleware

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',include(admin.site.urls)),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^price/$','priceList.views.price'),
    url(r'^products/$','prod.views.products'),
    url(r'^news/(\d*)/$','news.views.news'),
    url(r'^mail/$','mail.views.form_get'),
    url(r'^mail/post/$','mail.views.form_post'),
#    url(r'^$', 'bkz.views.main'),
#    url(r'^about/$', 'bkz.views.about'),
)


urlpatterns+= staticfiles_urlpatterns()