from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplemooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('simplemooc.core.urls', namespace='core')), # url sem prefixo http://127.0.0.1:8000/
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')), # url com prefixo cursos/ http://127.0.0.1:8000/cursos/
    url(r'^admin/', include(admin.site.urls)), # url com prefixo admin http://127.0.0.1:8000/admin/
)

if settings.DEBUG: # Se estiver no ambiente de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adiciona na urlpatterns a função static(URL base, diretorio ROOT dos arquivos)