from django.shortcuts import redirect, render
import sys
sys.path.append("..")
from accounts.models import UserProfile
from community.models import Community
from django.core.paginator import Paginator
# Create your views here.

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