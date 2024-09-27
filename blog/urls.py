from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name='login_page'),
    path('logout/', views.logoutuser, name='logout_page'),
    path('register/', views.registerpage, name='register_page'),
    path('',views.home, name='home_page'),
    path('room/<str:pk>/',views.room, name='room_page'),
    path('profile/<str:pk>/', views.profilepage, name = 'profile_page'),
    path('create_room/', views.createRoom, name="create_room"),
    path('update_room/<str:pk>/', views.updateRoom, name="update_room"),
    path('delete_room/<str:pk>/', views.deleteRoom, name="delete_room"),
    path('delete_message/<str:pk>/', views.deleteMessage, name="delete_message"),
    path('update_user/', views.updateuser, name="update_user"),
    path('topics/', views.updatetopics, name="topics"),
    path('activity/', views.activitypage, name="activity"),
    path('loggin_error/', views.room, name="loggin_error"),
]
