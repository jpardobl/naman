from models import (
    Project,
    Machine,
    Iface,
    DNSZone,
    Environment,
    VLan,
    Role,
    OperatingSystem,
    MType,
    ExcludedIPRange,
    Service,
    VLanConfig,
    )
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from serializers import (
    ProjectSerializer,
    MachineSerializer,
    IfaceSerializer,
    DNSZoneSerializer,
    EnvironmentSerializer,
    VLanSerializer,
    RoleSerializer,
    OperatingSystemSerializer,
    MTypeSerializer,
    ExcludedIPRangeSerializer,
    ServiceSerializer,
    VLanConfigSerializer)


class VLanConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VLanConfig.objects.all()
    serializer_class = VLanConfigSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ExcludedIPRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExcludedIPRange.objects.all()
    serializer_class = ExcludedIPRangeSerializer


class OperatingSystemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MachineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MType.objects.all()
    serializer_class = MTypeSerializer


class IfaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Iface.objects.all()
    serializer_class = IfaceSerializer


class DNSZoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DNSZone.objects.all()
    serializer_class = DNSZoneSerializer


class VLanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = VLan.objects.all()
    serializer_class = VLanSerializer


class EnvironmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

