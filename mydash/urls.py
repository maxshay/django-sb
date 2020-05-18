from django.urls import path
from . import views
from mydash.dash_apps.finished_apps import dashexample

urlpatterns = [
    path('', views.mydash, name='mydash')
]