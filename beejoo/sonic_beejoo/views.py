from django.shortcuts import render
from django.http import HttpResponse
from sonic_beejoo.forms import GoodForm, DesignTypeForm
from sonic_beejoo.models import DesignType


# Create your views here.
def design_type(request):
    if request.method == 'GET':
        des = DesignType.objects.all().filter(is_displayedd=True)
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





