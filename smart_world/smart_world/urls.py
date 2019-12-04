"""smart_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    # from here all the data from the sensor
    path('sensor_data/', views.getList),
    path('sensor_data/<int:pk>', views.detailList),
    path('sensor_data/put/<int:pk>', views.detailList),
    path('sensor_data/post/', views.postList),
    # from here all the urls from a specific sensor
    path('sensor/', views.sensorList),
    path('sensor/<int:sensor_id>/', views.sensorDetail),
    path('sensor/put/<int:sensor_id>/', views.sensorDetail),
    path('sensor/post/', views.sensorPost),
    # graph
    path('graph/', views.getGraph),
    path('graph/post/', views.postGraph),

]

urlpatterns = format_suffix_patterns(urlpatterns)