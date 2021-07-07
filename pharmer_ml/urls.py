"""pharmer_ml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, cropyield_view, cropvalue_view, temprf_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ 
    path('', home_view, name = 'home_view'),
    path('', include('pages.urls', namespace='pages')),
    path('pages/home', home_view, name = 'home_view'),
    path('pages/cropyeild', cropyield_view, name = 'cropyield_view'),
    path('pages/cropvalue', cropvalue_view, name = 'cropvalue_view'),
    path('pages/temprf', temprf_view, name = 'temprf_view'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()