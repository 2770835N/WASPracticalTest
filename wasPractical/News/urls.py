from django.urls import path
from News import views

app_name = 'News'

urlpatterns = [
    path('', views.title, name='title'),
]
