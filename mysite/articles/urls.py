from django.urls import path
# 밑의 . 은 내 현재 폴더를 의미한다.
from . import views
app_name = "articles"
# 경로에 이름을 지정해준 이유: 어디로 이동해야 되는지를 
# 수정해줘야 될 때 이 이름을 통해서 수정할 수 있도록 해주기 위해서이다.
urlpatterns = [
    # path('index/', views.index, name="index"),
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('introduce/', views.introduce, name="introduce"),
    path('detail/<int:article_pk>/', views.detail, name="detail"),
    path('<int:article_pk>/delete/', views.delete, name="delete"),
    path('<int:article_pk>/edit/', views.edit, name="edit"),
    path('<int:article_pk>/update/', views.update, name="update"),
]