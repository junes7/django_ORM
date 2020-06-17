from django.urls import path
# 밑의 . 은 내 현재 폴더를 의미한다.
from . import views
app_name = "jobs"

urlpatterns = [
    path('', views.index, name="index"),
    path('past_life/', views.past_life, name="past_life"),
]