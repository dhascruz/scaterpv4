
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from . import admin_views

urlpatterns = [

    path('', views.redirect_to_login),
    path('register/', views.register, name='register'),
    path('register_farmer_detail/<int:user_id>/', views.register_farmer_detail, name='register_farmer_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('/', views.adminhome, name='adminhome'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('outlet-dashboard/', views.outlet_dashboard, name='outlet-dashboard'),


     

    ###urls admin to add categories
   path('categories/', admin_views.category_list, name='category_list'),
    path('categories/new/', admin_views.category_create, name='category_create'),
    path('categories/edit/<int:id>/', admin_views.category_edit, name='category_edit'),
    path('categories/delete/<int:id>/', admin_views.category_delete, name='category_delete'),
    ###urls admin to add categories


    path('users_list', admin_views.user_list, name='user_list'),
    path('users/new/', admin_views.user_create, name='user_create'),
    path('users/edit/<int:id>/', admin_views.user_edit, name='user_edit'),
    path('users/delete/<int:id>/', admin_views.user_delete, name='user_delete'),


    path('farmer_asset_list/', admin_views.farmer_asset_list, name='farmer_asset_list'),
    path('assets/new/', admin_views.asset_create, name='asset_create'),
    path('assets/edit/<int:id>/', admin_views.asset_edit, name='asset_edit'),
    path('assets/delete/<int:id>/', admin_views.asset_delete, name='asset_delete'),


    path('farmer_product_list/', admin_views.farmer_product_list, name='farmer_product_list'),
    path('admin_product_create/', admin_views.admin_add_agri_product, name='add_agri_product'),
    path('admin_product/<int:pk>/edit/', admin_views.admin_agri_product_update, name='agri_product_update'),
    path('admin_product/<int:pk>/delete/', admin_views.admin_agri_product_delete, name='agri_product_delete'),
    #path('add-category/', admin_views.add_category, name='add_category'),


    #path('contact_list/', admin_views.farmer_contact_list, name='contact_list'),
    path('farmer_contact_list/', admin_views.farmer_contact_list, name='farmer_contact_list'),
    path('contacts/add/', admin_views.farmer_add_contact, name='add_contact'),
    path('contacts/<int:pk>/edit/', admin_views.farmer_edit_contact, name='edit_contact'),
    path('contacts/<int:pk>/delete/', admin_views.farmer_delete_contact, name='delete_contact'),



    ###urls admin to add farmers
   path('farmer_list/', views.farmer_list, name='farmer_list'),
    # path('categories/new/', views.category_create, name='category_create'),
    # path('categories/edit/<int:id>/', views.category_edit, name='category_edit'),
    # path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),
    # ###urls admin to add farmers


###urls admin to add farmer profiles
    
    # path('categories/new/', views.category_create, name='category_create'),
    # path('categories/edit/<int:id>/', views.category_edit, name='category_edit'),
    # path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),
    # ###urls admin to add farmer profiles

###urls admin to add farmer profiles
    
    # path('categories/new/', views.category_create, name='category_create'),
    # path('categories/edit/<int:id>/', views.category_edit, name='category_edit'),
    # path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),
    # ###urls admin to add farmer profiles


###urls admin to add farmer contact
   
    # path('categories/new/', views.category_create, name='category_create'),
    # path('categories/edit/<int:id>/', views.category_edit, name='category_edit'),
    # path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),
    # ###urls admin to add farmer profiles

    path('farmer/enable-2fa/', views.enable_two_factor, name='enable_two_factor'),
    path('farmer/disable-2fa/', views.disable_two_factor, name='disable_two_factor'),
    path('farmer/verify-2fa/', views.verify_totp, name='verify_totp'),




    path('farmer/personal_information/<int:user_id>/', views.personal_information, name='personal_information'),
    path('farmer/farmer_success/', views.farmer_success, name='farmer_success'),

    #path('farmer/personal_information', views.personal_information, name='personal_information'),
    #path('farmer/products', views.products, name='products'),
    path('farmer/projection', views.projection, name='projection'),


 #path('farmer/product_list', views.product_list, name='product_list'),
  #  path('farmer/product/new/', views.product_create, name='product_create'),
   # path('farmer/product/<int:pk>/edit/', views.product_update, name='product_update'),
   # path('farmer/product/<int:pk>/delete/', views.product_delete, name='product_delete'),


    path('farmer/product_create/', views.add_agri_product, name='add_agri_product'),
    path('farmer/product_list/', views.agri_product_list, name='agri_product_list'),
    path('farmer/product/<int:pk>/edit/', views.agri_product_update, name='product_update'),
    path('farmer/product/<int:pk>/delete/', views.agri_product_delete, name='product_update'),
    path('add-category/', views.add_category, name='add_category'),

   




    path('farmer/assets/', views.asset_list, name='asset_list'),
    path('farmer/assets/new/', views.asset_create, name='asset_create'),
    path('farmer/assets/edit/<int:id>/', views.asset_edit, name='asset_edit'),
    path('farmer/assets/delete/<int:id>/', views.asset_delete, name='asset_delete'),

     path('farmer/contact_list/', views.farmer_contact_list, name='contact_list'),
    path('farmer/contacts/add/', views.farmer_add_contact, name='add_contact'),
    path('farmer/contacts/<int:pk>/edit/', views.farmer_edit_contact, name='edit_contact'),
    path('farmer/contacts/<int:pk>/delete/', views.farmer_delete_contact, name='delete_contact'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

