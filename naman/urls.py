from django.conf.urls import url, patterns, include
from core.views import *
from rest_framework import viewsets, routers

from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'machines', MachineViewSet)
router.register(r'ifaces', IfaceViewSet)

router.register(r'dnszones', DNSZoneViewSet)
router.register(r'environments', EnvironmentViewSet)
router.register(r'operating_systems', OperatingSystemViewSet)
router.register(r'vlans', VLanViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'mtypes', MTypeViewSet)
router.register(r'excluded_ip_ranges', ExcludedIPRangeViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'vlan_config', VLanConfigViewSet)


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns("core.views",
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)


#urlpatterns = format_suffix_patterns(urlpatterns)

