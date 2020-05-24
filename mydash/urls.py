from django.urls import path
from . import views
from mydash.dash_apps.finished_apps import dashexample

urlpatterns = [
    path('', views.mydash, name='mydash'),
    path('get-call-test/', views.get_test, name='get-test'),
    path('get-call-test2/', views.get_test2, name='get-test2')
]