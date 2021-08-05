from django import forms
from .models import MyClothes


class MyClothesPost(forms.ModelForm):
    class Meta:
        model=MyClothes
        fields='__all__'

 