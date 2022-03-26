from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import PasswordResetView,SetPasswordForm
from tours import views
from django.contrib.auth import views as auth_views
from tours.form import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('login', views.user_login,name="login"),
    path('registration', views.registration,name="registration"),
    path('logout', views.user_logout,name="logout"),

    path("password-reset",auth_views.PasswordResetView.as_view(template_name="password-reset.html",form_class=Password_reset),name="password_reset"),
    path("password-reset/Done",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_Confirm.html",form_class=Password_confirm), name="password_reset_confirm"),

    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_Complete.html"),name="password_reset_complete"),


    #user
    path('index', views.user_index,name="user_index"),
    path('payment/<int:id>', views.payment,name="payment"),
    path('place_detail/<int:id>', views.place_detail,name="place_detail"),
    path('booked', views.booked,name="booked"),
    path('delete-booking/<int:id>', views.delete_booking,name="delete_booking"),


    #Admin
    path('add-place', views.add_place,name="add_place"),
    path('Dashboard', views.Dashboard,name="Dashboard"),
    path('place-list', views.place_list,name="place_list"),
    path('customer-list', views.customer_list,name="customer_list"),
    path('delete-payment/<int:id>', views.delete_payment,name="delete_payment"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
