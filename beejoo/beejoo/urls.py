"""beejoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from sonic_beejoo.views import design_type, category, color, add_goods, goods


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^design/', design_type, name='create_des'),
    url(r'^category/', category, name='create_cat'),
    url(r'^color/', color, name='create_col'),
    url(r'^add/', add_goods, name='add_good'),
    url(r'^$', goods, name='index'),
    url(r'^users/', include('sb_auth.urls', namespace='sb_auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
