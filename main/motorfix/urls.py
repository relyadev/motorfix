"""
URL configuration for motorfix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main, name = "main"),

    path("garage/", views.garage, name = "garage"),
    path("garage/add", views.add_car, name = "add_car"),
    path("garage/delete/<int:id>", views.delete_car, name = "car_delete"),

    path("order/", views.order, name = "order"),
    path("order/add", views.make_order, name = "add_order"),

    path("history/", views.history, name = "history"),
    ######
    path('admin/', admin.site.urls),
    path('auth/registration/', views.registration, name = "registration"),
    path("auth/login", views.EmailLogin.as_view(), name="login")

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)