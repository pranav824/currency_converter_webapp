from django.urls import path
from .views import index

app_name = 'converter'

urlpatterns = [
    path('', index, name='index'),
]
