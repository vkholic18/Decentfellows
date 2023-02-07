from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Video,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import MyUserCreationForm, MyUserProfileForm,ProfilePicForm,FeedbackForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Profile
from django.core.paginator import Paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from .forms import VideoForm


@login_required(login_url='/login')
def index(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            return redirect('feed')
    else:
        form = VideoForm()
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 6) # Show 6 videos per page
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'page_obj': page_obj, 'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        profile_form = MyUserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
        profile_form = MyUserProfileForm()
    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})

# Create your views here.



def home(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,"landing.html",context)


@login_required(login_url='/login')
def profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilePicForm(instance=profile)
    
    user = request.user
    print(user.username)
    videos=Video.objects.filter(uploaded_by=user)
    return render(request,"profile.html",{'form': form, 'profile': profile,'videos': videos})

def detail_profile(request,id):
    profile=Profile.objects.get(id=id)
    context={'profile':profile}
    return render(request,'profile_detail.html',context)

@login_required(login_url='/login')
def members(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    context = {'profiles': profiles, 'form': form}
    return render(request, 'members.html', context)







