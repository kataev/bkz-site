from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'bkz.views.main'),
    url(r'^about/$', 'bkz.views.about'),
)
