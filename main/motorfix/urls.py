from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main, name = "main"),

    path("garage/", views.garage, name = "garage"),
    path("garage/add", views.add_car, name = "add_car"),
    path("garage/delete/<int:id>", views.delete_car, name = "car_delete"),
    path("garage/update/<int:id>", views.update_car, name = "car_update"),

    path("order/", views.order, name = "order"),
    path("order/add", views.make_order, name = "add_order"),

    path("history/", views.history, name = "history"),
    ########################################################
    path('admin/', admin.site.urls),
    path('auth/registration/', views.registration, name = "registration"),
    path("auth/login", views.EmailLogin.as_view(), name="login")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = "app.views.handler404"
handler403 = "app.views.handler403"

