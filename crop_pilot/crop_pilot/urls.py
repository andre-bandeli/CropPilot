
from django.contrib import admin
from django.urls import path
from routes.views import RouteOptimizationAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/optimize/', RouteOptimizationAPI.as_view(), name='optimize-route'),

]
