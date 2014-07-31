from naman.core.models import VLan
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_staff)
def get_free_ip_by_vlan(request, vlan_id):

    vlan = get_object_or_404(VLan, id=vlan_id)

    return render(
        request,
        "vlan/free_ip.json",
        {"free_ip": vlan.get_ip()},
        content_type="application/json"
    )