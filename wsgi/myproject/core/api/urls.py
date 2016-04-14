from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.api.views',
    url(r'^hola_mundo_rest/(?P<nombre>\w+)$', 'hola_mundo'),
    url(r'^usuarios/$', 'usuarios'),
    url(r'^usuarios/(?P<id>\d+)$', 'usuarios'),
    url(r'^todos/$', 'to_do'),
)