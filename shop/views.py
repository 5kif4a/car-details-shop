from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.db.models import Q
import shop.models as mdl


# Create your views here.
def nav(request):
    page_name = request.get_full_path()
    if page_name == '/':
        return render(request, 'shop/main.html', {})
    return render(request, 'shop/{}.html'.format(page_name), {})


def search(request):
    if request.method == 'POST':
        req = request.POST.get('search')
        results = mdl.Detail.objects.filter(Q(vehicle_id__name__contains=req) |
                                            Q(vehicle_id__mark_id__name__contains=req) |
                                            Q(name__contains=req))
        return render(request, 'shop/search.html', {'results': results})


def car(request, mark):
    return HttpResponse(mark)


def category(request, category):
    try:
        category_name = mdl.DetailType.objects.get(link_name=category)
        products = mdl.Detail.objects.filter(detail_type_id__name=category_name)
        return render(request, 'shop/category.html', {'products': products,
                                                      'category': category_name})
    except mdl.DetailType.DoesNotExist:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def report(request):
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['comment']
        r = mdl.Report.objects.create(
            name=name,
            text=comment
        )
        r.save()
        return HttpResponse('')
