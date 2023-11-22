from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('user/profile/', views.user_detail, name='userdetail'),
    path('user/chart/', views.profile_chart, name='profilechart'),
    path('user/update/', views.update, name='update'),
    path('user/recommend/', views.recommend_products, name='recommend_products'),
]
