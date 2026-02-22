from django.contrib import admin
from django.urls import path, include

# url -- "misamarti" , endpoint, "marshuti"
# python manage.py createsuperuser
urlpatterns = [
    path('admin/', admin.site.urls),
    path("app1/", include("app1.urls")),
]
