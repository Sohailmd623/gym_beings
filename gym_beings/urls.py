from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gym/', include('gym.urls')),
    path('', include('fox.urls')),
]