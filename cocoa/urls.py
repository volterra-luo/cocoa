from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cocoa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^alipay/',include('alipay.urls', namespace='alipay')),
    url(r'^admin/', include(admin.site.urls)),
)
