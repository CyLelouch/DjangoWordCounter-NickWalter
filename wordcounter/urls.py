

from django.urls import path
from . import views


urlpatterns = [
    path('homePage', views.homePage),
    path('count',views.count),
    path('about',views.about),
]
