from django.contrib import admin
from django.urls import path, include
from untitled import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/', include('badday.urls'))
]
