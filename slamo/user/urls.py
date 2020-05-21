from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signin),
    path('signup', views.signup),
    path('signin', views.signin),
    path('signout', views.signout),
    path('forget_pass/',auth_views.PasswordResetView.as_view(template_name='user/forget_pass.html'),
        ),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/pass_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/pass_rest_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='user/pass_reset_complete.html'),
         name='password_reset_complete'),
]
