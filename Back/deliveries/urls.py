from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create), # 생성
    path('', views.get_deliveries), # 관리자 메인페이지 데이터 
    path('user/main/', views.get_deliveries_mine), # 유저 메인페이지 데이터
    path('detail/', views.get_detail_deliveries), # 상세페이지 데이터
    path('move/', views.move), # 상태변화
    path('search/detail/location/', views.search_detail_location), # 검색 - 상세페이지
    path('search/detail/user/', views.search_detail_user),
    path('search/detail/number/', views.search_detail_number),
    path('search/location/', views.search_location), # 검색 - 메인페이지
    path('search/user/', views.search_user),
    path('address/', views.get_address), # 현재 등록되어 있는 주소 반환
    path('alarm/create/', views.create_alarm), # 알람 생성
    path('alarm/', views.alarm), # 알람 조회
    path('alarm/delete/', views.alarm_delete), # 알람 삭제
    path('alarm/view/', views.alarm_view), # 알람확인
    path('alarm/check/', views.alarm_check), # 신규 알람 체크
    path('chart/data/', views.get_chart_data), # 차트 데이터 반환
    path('chart/data/2', views.get_chart_data_d), # 차트 데이터 반환
]  