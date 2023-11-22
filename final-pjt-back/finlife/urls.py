from django.urls import path
from . import views

urlpatterns = [
    path('d/', views.d_index),
    # 전체 정기예금 상품 목록 출력 & DB 저장
    path('s/', views.s_index),
    # 전체 정기적금 상품 목록 출력 & DB 저장
    path('deposit-detail/<str:fin_prdt_cd>/', views.deposit_detail),
    # 특정 예금상품의 상세정보 출력
    path('saving-detail/<str:fin_prdt_cd>/', views.saving_detail),
    # 특정 적금상품의 상세정보 출력
    path('deposit-sort/<int:sort_num1>/', views.deposit_sort),
    path('deposit-sort/<int:sort_num1>/<int:sort_num2>/', views.deposit_sort),
    # 필터링된 정기예금 정보
    path('saving-sort/<int:sort_num1>/', views.saving_sort),
    path('saving-sort/<int:sort_num1>/<int:sort_num2>/', views.saving_sort)
    # 필터링된 정기적금 정보
]