from django.contrib import admin
from django.urls import path, include
from warehouse.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('warehouse.urls')),
    path('', IndexView.as_view(), name='index'), 
]
