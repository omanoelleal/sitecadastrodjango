# from django.contrib import admin
from django.urls import path
from app_cad_users import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', views.home, name='home'),
]