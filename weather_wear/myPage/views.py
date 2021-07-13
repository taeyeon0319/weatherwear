from .models import MyClothes
from django.shortcuts import get_object_or_404, redirect, render
import sys
sys.path.append("..")
from accounts.models import UserProfile
from community.models import Community
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView
# Create your views here.

class ClothesListView(ListView):
    model=MyClothes


#마이페이지로 이동하는 함수
def mypage(request):
    return render(request, 'myPage/myPageMain.html')

#개인정보 페이지로 이동하는 함수
def profile(request):
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    return render(request, 'myPage/myPageProfile.html', {'profiles':profiles})

#개인정보 수정 화면 연결 함수
def edit_profile(request):
    check = request.user
    profiles = UserProfile.objects.get(user = check)
    return render(request, 'myPage/edit_profile.html', {'profiles':profiles})

#수정된 개인정보
def update_profile(request):
    check = request.user
    update_profiles = UserProfile.objects.get(user = check)
    update_profiles.name = request.POST['name']
    update_profiles.email = request.POST['email']
    check.email = request.POST['email']
    update_profiles.gender = request.POST['gender']
    update_profiles.height = request.POST['height']
    update_profiles.bodyForm = request.POST['bodyForm']
    update_profiles.save()
    check.save()
    return redirect('myPage:profile')

# 커뮤니티에 작성한 글 페이지 나타나내는 함수
def writing_list(request):
    user = request.user
    selected_weather = "날씨전체"
    community = Community.objects.filter(writer = user).order_by('-pub_date')
    count = 0
    for i in community:
        count += 1
    page = int(request.GET.get('p',1))
    paginator = Paginator(community,3)
    boards = paginator.get_page(page)
    return render(request, 'myPage/writing_list.html',{'boards':boards, 'count':count,'selected_weather':selected_weather })

def filter_list(request):
    count = 0
    user = request.user
    if request.method == "POST":
        selected_weather = request.POST['weather']
        if selected_weather == "날씨전체":
            community = Community.objects.filter(writer = user).order_by('-pub_date')
            for i in community:
                count += 1
        else:
            community = Community.objects.filter(writer = user, weather = selected_weather).order_by('-pub_date')
            for i in community:
                count += 1
    page = int(request.GET.get('p',1))
    paginator = Paginator(community,3)
    boards = paginator.get_page(page)
    return render(request,'myPage/writing_list.html',{'boards':boards, 'count':count,'selected_weather':selected_weather })
#자기착장페이지로 이동
def my_clothes(request):
    user=request.user
    clothes=MyClothes.objects.filter(user=user).order_by('-post_date')
    check=request.user.email
    profiles=UserProfile.objects.get(email=check)
    selected_weather="all"
    page=int(request.GET.get('p',1))
    paginator=Paginator(clothes, 3)
    boards=paginator.get_page(page)
    return render(request, 'myPage/my_clothes.html',{'profiles':profiles, 'clothes':clothes, 'boards':boards , 'selected_weather':selected_weather})

#글쓰기
def new_clothes(request):
    check=request.user.email
    profiles=UserProfile.objects.get(email=check)
    return render(request, 'myPage/new_clothes.html',{'profiles':profiles})

#착장만들기
def create_clothes(request):
    new_clothes=MyClothes()
    new_clothes.title=request.POST['title']
    new_clothes.weather=request.POST['category_radio']
    new_clothes.temperature=request.POST['temperature']
    new_clothes.post_date=datetime.today()
    new_clothes.thumbnail=request.FILES.get('thumbnail')
    new_clothes.user=request.user
    new_clothes.memo=request.POST['memo']
    new_clothes.save()
    return redirect('myPage:my_clothes')

def detail_clothes(request, id):
    clothes=get_object_or_404(MyClothes,pk=id)
    return render(request, 'myPage/detail_clothes.html',{'clothes':clothes})

 
def delete_clothes(request,id):
    delete=MyClothes.objects.get(id=id)
    delete.delete()
    return redirect('myPage:my_clothes')


def edit_clothes(request,id):
    edit=MyClothes.objects.get(id=id)
    return render(request, 'myPage/edit_clothes.html',{'clothes':edit})

def update_clothes(request, id):
    update_clothes=MyClothes()
    update_clothes.title=request.POST['title']
    update_clothes.weather=request.POST['category_radio']
    update_clothes.temperature=request.POST['temperature']
    update_clothes.post_date=datetime.today()
    update_clothes.thumbnail=request.FILES.get('thumbnail')
    update_clothes.user=request.user
    update_clothes.memo=request.POST['memo']
    update_clothes.save()
    return redirect('myPage:detail_clothes',update_clothes.id)

#날씨따라 분류
def filter_clothes(request):
    user = request.user
    if request.method == "POST":
        selected_weather = request.POST['weather']
        if selected_weather == "all": 
            return redirect('myPage:my_clothes')
        else:
            clothes=MyClothes.objects.filter(user=user, weather=selected_weather).order_by('-post_date')
            check=request.user.email
            profiles=UserProfile.objects.get(email=check)
            page=int(request.GET.get('p',1))
            paginator=Paginator(clothes, 3)
            boards=paginator.get_page(page)
            return render(request, 'myPage/my_clothes.html',{'profiles':profiles, 'clothes':clothes, 'boards':boards, "selected_weather":selected_weather})


def filter_temp(request, selected_weather): #selected_weather값 받음 >> template수정, url도 포함
    user=request.user
    temp=int(request.POST['temp'])#temp로 폼구성
    if request.method=='POST':
        if selected_weather=='all':
                clothes=MyClothes.objects.filter(user=user, temperature__gte=(temp-2),temperature__lte=(temp+2))
        else:
                clothes=MyClothes.objects.filter(user=user, temperature__gte=(temp-2), temperature__lt=(temp+2),weather=selected_weather)
    check=request.user.email
    profiles=UserProfile.objects.get(email=check)
    page=int(request.GET.get('p',1))
    paginator=Paginator(clothes, 3)
    boards=paginator.get_page(page)
    return render(request, 'myPage/my_clothes.html',{'profiles':profiles, 'clothes':clothes, 'boards':boards, "selected_weather":selected_weather})

