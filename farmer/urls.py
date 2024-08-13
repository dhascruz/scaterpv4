from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_farmer_detail/<int:user_id>/', views.register_farmer_detail, name='register_farmer_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('/', views.adminhome, name='adminhome'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),


    path('farmer/personal_information/<int:user_id>/', views.personal_information, name='personal_information'),
    path('farmer/farmer_success/', views.farmer_success, name='farmer_success'),

    #path('farmer/personal_information', views.personal_information, name='personal_information'),
    path('farmer/products', views.products, name='products'),
    path('farmer/projection', views.projection, name='projection'),
    path('farmer/my_contacts', views.my_contacts, name='my_contacts'),


]
