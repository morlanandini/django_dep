from app1 import views
from django.urls import path,include
app_name='app1'
urlpatterns = [
path('', views.home,name='home'),
path('reg/',views.reg,name='reg'),
path('logins/',views.user_login,name='user_login'),
path('logout/',views.user_logout,name='user_logout')
]
