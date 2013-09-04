from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


def paginator(queryset, request, objs_per_page=None):
    paginator = Paginator(queryset, settings.RESULTS_PER_PAGE if objs_per_page == None else objs_per_page)
    page = request.GET['page'] if 'page' in request.GET and request.GET['page'] != None else 1

    try:
        return paginator.page(page)
    except PageNotAnInteger:
        messages.add_message(request, messages.ERROR, 'Invalid page, showing page number 1')
        return paginator.page(1)
    except EmptyPage:
        messages.add_message(request, messages.ERROR, 'Invalid page, showing last one')
        return paginator.page(paginator.num_pages)
