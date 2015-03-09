from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quotes.views.quote', name='home'),
    url(r'^add/$', 'quotes.views.add_quote', name='add'),
    url(r'^thanks/$', 'quotes.views.thanks', name='thanks'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
