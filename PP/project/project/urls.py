from django.contrib import admin
from django.urls import path

# url -- "misamarti" , endpoint, "marshuti"
# python manage.py createsuperuser
urlpatterns = [
    path('admin/', admin.site.urls),
]
