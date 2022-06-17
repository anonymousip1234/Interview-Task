from . import views

from django.urls import path


urlpatterns = [
    path('',views.Index,name = 'index'),
    path('report/',views.reports,name = 'reports'),
    path('logout/',views.logout,name = 'logout')
]