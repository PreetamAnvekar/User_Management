from django.urls import path
from .views import users_list_create


urlpatterns = [
    path('', users_list_create, name='users'),

]
