from django.urls import path
from . import views

app_name = "myPage"
urlpatterns = [
    path('',views.mypage, name="mypage"),
    path('profile/', views.profile, name="profile"),
    path('edit/', views.edit_profile, name="edit"),
    path('update/', views.update_profile, name="update"),
]
    
