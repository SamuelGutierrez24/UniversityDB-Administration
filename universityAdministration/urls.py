"""
URL configuration for universityAdministration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from EventsDB.views import menu;
from EventsDB.views import register_events
from EventsDB.views import register_person


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',menu.menu),
    path('registerEvent1/',register_events.register1,name='rEvents_a'),
    path('registerEvent2/',register_events.register2,name='rEvents_b'),
    path('registerUser/',register_person.register1,name='rUser'),




]
