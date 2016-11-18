from django.shortcuts import render
from django.http import HttpResponse
from sonic_beejoo.forms import GoodForm, DesignTypeForm
from sonic_beejoo.models import DesignType

# Create your views here.
def design_type(request):
    if request.method == 'GET':
        form = DesignTypeForm()
        render(request,'sonic_beejoo/attributes.html', {'design': form})
    elif request.method == 'POST':
        form = DesignTypeForm(request.POST)
        if form.is_valid():
            form.save()
        render(request,'sonic_beejoo/attributes.html', {'design': form})

    return HttpResponse(status=405)





