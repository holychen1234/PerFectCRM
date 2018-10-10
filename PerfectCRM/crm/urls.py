from django.conf.urls import url,include
from crm import views

urlpatterns = [
    url(r'^$', views.dashboard, name='sales_dashboard'),
    url(r'^login/', views.acc_login, name='login'),
    url(r'^logout/', views.acc_logout, name='logout'),
    url(r'^response/', views.response, name='response'),
    url(r'^info/', views.info, name='info'),
    url(r'^test1/', views.test1, name='test1'),
]