from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import UserProfile

class SignupForm(forms.Form):
    class Meta:
        model = User

    GENDER_CHOICE = (
        ('남자', '남자'),
        ('여자', '여자'),
    )
    BODY_FORM = (
        ('마름','마름'),
        ('보통','보통'),
        ('과체중','과체중'),
    )

    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}), label="이름")
    gender = forms.ChoiceField(choices= GENDER_CHOICE, label="성별", widget=forms.Select)
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placehoder':''}), label="나이")
    height = forms.IntegerField(widget=forms.TextInput(attrs={'placehoder':''}), label="키")
    bodyForm = forms.ChoiceField(choices= BODY_FORM, label="체형", widget=forms.Select)

    def signup(self, request, user):
        userProfile = UserProfile()
        userProfile.user = user
        userProfile.name = self.cleaned_data[('name')]
        userProfile.email = user.email
        userProfile.gender = self.cleaned_data[('gender')]
        userProfile.age = self.cleaned_data[('age')]
        userProfile.height = self.cleaned_data[('height')]
        userProfile.bodyForm = self.cleaned_data[('bodyForm')]
        userProfile.save()
        user.save()
        return user