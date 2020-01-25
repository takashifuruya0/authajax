
from django.urls import include, path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('signin', views.signin_view, name='signin'),
    path('signup', views.signup_view, name='signup'),
    path('signout', views.signout_view, name='signout'),
    path('ajaxlogin', views.ajax_login, name='signin_ajax')
]