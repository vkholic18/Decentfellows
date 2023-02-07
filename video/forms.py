from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Video,Feedback
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class MyUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'location')
        
class  ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['caption', 'video']
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']