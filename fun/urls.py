from django.conf.urls import patterns, url, include
from rest_framework import routers
from fun import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'jokes', views.JokeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += patterns('',
	url(r'^index/$', views.index),
)
