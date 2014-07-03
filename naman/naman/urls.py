from django.conf.urls import url, patterns, include
from naman.core.views import *

from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
#router.register(r'machines', MachineViewSet)
#router.register(r'ifaces', IfaceViewSet)

router.register(r'dnszones', DNSZoneViewSet)
router.register(r'environments', EnvironmentViewSet)
router.register(r'operating_systems', OperatingSystemViewSet)
router.register(r'vlans', VLanViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'mtypes', MTypeViewSet)
router.register(r'excluded_ip_ranges', ExcludedIPRangeViewSet)
router.register(r'services', ServiceViewSet)
#router.register(r'vlan_config', VLanConfigViewSet)


urlpatterns = patterns("core.views",
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^api/vlanconfigs/(?P<pk>[0-9]+)/$', VLanConfigDetail.as_view(), name='vlanconfig-detail'),
    url(r'^api/vlanconfigs/$', VLanConfigList.as_view(), name='vlanconfig-list'),
    url(r'^api/machines/(?P<pk>[0-9]+)/$', MachineDetail.as_view(), name='machine-detail'),
    url(r'^api/machines/$', MachineList.as_view(), name='machine-list'),
    url(r'^api/ifaces/(?P<pk>[0-9]+)/$', IfaceDetail.as_view(), name='iface-detail'),
    url(r'^api/ifaces/$', IfaceList.as_view(), name='iface-list'),
    
    url(r'^api/', include(router.urls)),

    url(r'^admin/?', include(admin.site.urls)),
    
    
    url(r'^', include("web.urls")),
)


#urlpatterns = format_suffix_patterns(urlpatterns)

