"""
URL configuration for project_k project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from basic.views import sample
from basic.views import shopping
from basic.views import sampleInfo
from basic.views import dynamicResponse
from basic.views import sum
from basic.views import subtract
from basic.views import health,addstudent,addpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',sample),
    path('shopping/',shopping),
    path('info/',sampleInfo),
    path('dynamic/',dynamicResponse),
    path('sum/',sum),
    path('sub/',subtract),
    path('health/',health),
    path('addstudent/',addstudent),
    path('addpost/',addpost)
]
