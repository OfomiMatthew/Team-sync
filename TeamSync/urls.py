from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('team/',views.team_sync,name='team'),
]
 