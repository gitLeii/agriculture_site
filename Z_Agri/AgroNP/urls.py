from django.urls import path
from . import views as agro_views

urlpatterns = [
    path('', agro_views.index, name='index')
]