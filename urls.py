from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('',views.index,name="index"),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('store/', views.store, name='store'),
    path('blog/', views.blog, name='blog'),




    path('gallery/',views.gallery,name='gallery'),
    path('photo/<str:pk>',views.viewPhoto,name='photo'),
    path('add/',views.addPhoto,name='add'),

]


