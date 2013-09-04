#from django.contrib.auth.decorators import login_required
from django.shortcuts import render


#@login_required
def iface(request):
    return render(request, 'js/iface.js', content_type='application/javascript')


def vlanconfig(request):
    return render(request, 'js/vlanconfig.js', content_type='application/javascript')
