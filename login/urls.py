from django.contrib import admin
from django.urls import path, re_path
import app.views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', app.views.home, name='home'),
]
