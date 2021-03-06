from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from sonic_beejoo.forms import GoodForm, DesignTypeForm, CategoryForm, ColorForm
from sonic_beejoo.models import DesignType, Category, Color, Good


# Create your views here.
def design_type(request):
    if request.method == 'GET':
        des = DesignType.objects.all().filter(is_displayed=True)
        form = DesignTypeForm()
        c = {'designs': des, 'form': form}
        return render(request,'sonic_beejoo/attributes.html', c)
    elif request.method == 'POST':
        des = DesignType.objects.all()
        form = DesignTypeForm(request.POST)
        c = {'designs': des, 'form': form}
        if form.is_valid():
            form.save()
        return render(request,'sonic_beejoo/attributes.html', c)
    return HttpResponse(status=405)

def category(request):
    if request.method == 'GET':
        des = Category.objects.all().filter(is_displayed=True)
        form = CategoryForm()
        c = {'designs': des, 'form': form}
        return render(request,'sonic_beejoo/attributes.html', c)
    elif request.method == 'POST':
        des = Category.objects.all()
        form = CategoryForm(request.POST)
        c = {'designs': des, 'form': form}
        if form.is_valid():
            form.save()
        return render(request,'sonic_beejoo/attributes.html', c)
    return HttpResponse(status=405)


def color(request):
    if request.method == 'GET':
        des = Color.objects.all().filter(is_displayed=True)
        form = ColorForm()
        c = {'designs': des, 'form': form}
        return render(request,'sonic_beejoo/attributes.html', c)
    elif request.method == 'POST':
        des = Color.objects.all()
        form = ColorForm(request.POST)
        c = {'designs': des, 'form': form}
        if form.is_valid():
            form.save()
        return render(request,'sonic_beejoo/attributes.html', c)
    return HttpResponse(status=405)


def add_goods(request):
    if request.method == 'GET':
        form = GoodForm()
        return render(request, 'sonic_beejoo/goods.html', {'form': form})
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'sonic_beejoo/goods.html', {'form': form})
    return HttpResponse(status=405)


def goods(request):
    if request.method == 'GET':
        in_basket = str(len(request.session['inbasket'])) if 'inbasket' in request.session else 0
        # visible_goods = Good.objects.all().select_related().prefetch_related(
        #     'colors', 'design_types', 'category'
        # ).first()
        visible_goods = Good.objects.all()
        return render(request, 'sonic_beejoo/product.html', {'goods': visible_goods, 'inbasket': in_basket})
    return HttpResponse(status=405)


def good(request, product_id):
    if request.method == 'GET':
        in_basket = str(len(request.session['inbasket'])) if 'inbasket' in request.session else 0
        return render(request, 'sonic_beejoo/good.html', {'goood': Good.objects.get(id=product_id), 'inbasket': in_basket})
    return HttpResponse(status=405)


def add_to_cart(request):
    if request.method == 'POST':
        if 'inbasket' not in request.session:
            request.session['inbasket'] = []
        request.session['inbasket'] += [request.POST['product']]
        return JsonResponse({'items_in_basket': str(len(request.session['inbasket']))})
    else:
        return redirect('/')


def basket(request):
    pass