
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Maxiapp/', include("Maxiapp.urls")),
    path("",include("Maxiapp.urls"))
]
