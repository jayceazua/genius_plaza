from django.contrib import admin
# from django.conf.urls import url, include
from django.urls import path, include

urlpatterns = [
    path('', include('recipes.urls')),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
]
