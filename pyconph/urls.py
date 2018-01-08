from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from pyconph.program.views import cfp, cfp_thanks
from pyconph.web.views import index



urlpatterns = [
    url(r'^cfp/$', cfp, name='cfp'),
    url(r'^cfp/thanks/$', cfp_thanks, name='cfp_thanks'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
