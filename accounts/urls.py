
from django.urls import include, path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signout/', views.SignoutView.as_view(), name='signout'),
    path('ajaxlogin/', views.ajax_login, name='signin_ajax')
]