from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.core.views',

    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)