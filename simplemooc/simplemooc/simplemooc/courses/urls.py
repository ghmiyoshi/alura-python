from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'details', name='details'), # (?P<pk>\d+) - Expressão regular
                                                       # <pk> Parâmetro nomeado para formar grupos
                                                       # \d+ Significa que na expressão regular deve entrar qualquer valor inteiro
)