from django.contrib import admin
from django.urls import path, include
from Main.views import welcome, locations

# URL patterns handled by the main welcome view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),
    path('locations', locations, name="locations"),
    path('session/', include('DataModels.urls')),
]
