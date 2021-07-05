from django.urls import path
from . import views

app_name = "myPage"
urlpatterns = [
    path('',views.mypage, name="mypage"),
    path('profile/', views.profile, name="profile"),
    path('edit/', views.edit_profile, name="edit"),
    path('update/', views.update_profile, name="update"),
    path('writing_list/', views.writing_list, name="writing_list"),
    path('filter_list/', views.filter_list, name="filter_list"),
    path('myclothes/', views.my_clothes, name='my_clothes'),
    path('newclothes/', views.new_clothes, name='new_clothes'),
    path('createclothes/',views.create_clothes, name='create_clothes'),
    path('<str:id>',views.detail_clothes, name="detail_clothes"),
    path('edit/<str:id>', views.edit_clothes, name='edit_clothes'),
    path('delete/<str:id>', views.delete_clothes, name='delete_clothes'),
    path('update/<str:id>',views.update_clothes, name="update_clothes"),
    path('filterclothes/', views.filter_clothes, name='filter_clothes'),
    path('filtertemp/<str:selected_weather>',views.filter_temp,name='filter_temp'),
]
    
