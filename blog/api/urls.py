from django.urls import path
from .import views

urlpatterns = [
    path ('',views.getroutes,name = 'get_routes'),
    path ('rooms/',views.getrooms,name = 'get_rooms'),
    path ('rooms/<str:pk>',views.getroom,name = 'get_rooms'),
]
