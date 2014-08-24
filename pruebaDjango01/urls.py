from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebaDjango01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','app1.views.inicio'),
    url(r'^admin/', include(admin.site.urls)),

)
