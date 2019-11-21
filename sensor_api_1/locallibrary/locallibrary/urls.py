"""locallibrary URL Configuration

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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('stocks/', views.StockList.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns((urlpatterns))

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', views.getList),
    path('stocks/<int:pk>', views.detailList),
    path('stocks/v1/<int:pk>', views.putList),
    path('stocks/post/', views.postList),
    path('stocks/post3/<slug:ticker>/<int:open>/<int:close>/<int:volume>/', views.postList),
]
#
# ticker = models.CharField(max_length=10)
# open = models.FloatField()
# close = models.FloatField()
# volume = models.IntegerField()

urlpatterns = format_suffix_patterns(urlpatterns)


