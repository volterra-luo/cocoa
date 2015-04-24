from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.contrib import admin
admin.autodiscover()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cocoa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^alipay/',include('alipay.urls', namespace='alipay')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-fun/', include('fun.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cocoa.views.home', name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
