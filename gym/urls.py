from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),

    path('add_enq/', views.add_enq, name='add_enq'),
    path('recd_enq/', views.recd_enq, name='recd_enq'),
    path('delete_enq(?P<int:pk>)', views.delete_enq, name='delete_enq'),

    path('add_plan/', views.add_plan, name='add_plan'),
    path('membership_plan/', views.membership_plan, name='membership_plan'),
    path('delete_plan(?P<int:pk>)', views.delete_plan, name='delete_plan'),

    path('add_equip/', views.add_equip, name='add_equip'),
    path('recd_equip/', views.recd_equip, name='recd_equip'),
    path('delete_equip(?P<int:pk>)', views.delete_equip, name='delete_equip'),

    path('add_member/', views.add_member, name='add_member'),
    path('recd_member/', views.recd_member, name='recd_member'),
    path('delete_member(?P<int:pk>)', views.delete_member, name='delete_member'),

    path('thank_you', views.thank_you, name='thank_you'),

]