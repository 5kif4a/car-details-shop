from django.urls import path
from . import views


urlpatterns = [
    path('', views.nav),
    path('report', views.report),
    path('search', views.search),
    path('cars/<mark>', views.car),
    path('categories/<category>', views.category)
]
