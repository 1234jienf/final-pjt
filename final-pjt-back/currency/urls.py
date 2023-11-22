from django.urls import path
from . import views

app_name="currency"
urlpatterns = [
    path('exchange/', views.exchange, name="exchange"),
    path('to_kor/', views.to_kor, name="to_kor"),
    path('kor_to/', views.kor_to, name="kor_to"),
]