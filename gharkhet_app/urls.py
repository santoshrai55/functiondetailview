from django.urls import path
from . import views
app_name = "gharkhet_app"


urlpatterns = [
    path('', views.home, name="home"),
    path('home/<str:item>', views.home_detail, name="detail"),
]
