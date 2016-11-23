from django.shortcuts import render
from django.http import HttpResponse
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
        visible_goods = Good.objects.all()
        colors = visible_goods.colors.all()
        return render(request, 'sonic_beejoo/product.html', {'goods': visible_goods, 'colors': colors})


