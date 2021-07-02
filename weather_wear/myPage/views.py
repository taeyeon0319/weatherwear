from django.shortcuts import redirect, render
import sys
sys.path.append("..")
from accounts.models import UserProfile
# Create your views here.

#마이페이지로 이동하는 함수
def mypage(request):
    return render(request, 'myPage/myPageMain.html')

#개인정보 페이지로 이동하는 함수
def profile(request):
    check = request.user.email
    profiles = UserProfile.objects.get(email = check)
    return render(request, 'myPage/myPageProfile.html', {'profiles':profiles})

def edit_profile(request):
    check = request.user
    profiles = UserProfile.objects.get(user = check)
    return render(request, 'myPage/edit_profile.html', {'profiles':profiles})

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