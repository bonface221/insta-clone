from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm,NewPostForm
from .models import Post,Profile,Comment,Followers

# Create your views here.
def registerPage(request):  
    form = NewUserForm()

    if request.method =='POST':
        form= NewUserForm(request.POST)
        if form.is_valid():          
            user=form.save()
            profile=Profile(user=user)
            profile.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return redirect('home')
    
        messages.error(request, "Invalid username or Password, use strong password.")
            
    context=dict(form=form)
    return render(request,'base/registration/register.html',context)


def loginPage(request):
    if request.method == 'POST': 
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username').lower()
            password=request.POST.get('password')

            try:
                user = User.objects.get(username)

            except:
                messages.error(request,"Invalid username or password.")

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            messages.error(request,"Invalid username or password.")
        messages.error(request,"Invalid username or password.")

    context=dict()
    return render(request, 'base/registration/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url=('login'))
def home (request):
    posts=Post.objects.all()
    
    context=dict(posts=posts)
    return render(request,'base/home.html',context)

@login_required(login_url=('login'))
def profile(request,pk):
    profile= Profile.objects.get(user=pk)
    following = Followers.objects.filter(user=profile.id)
    followers = Followers.objects.filter(another_user=profile.user)
    posts=profile.post_set.all()

    context = {'posts':posts,'profile':profile,'followers':followers, 'following': following}
    return render(request,'base/profile.html',context)
    
@login_required(login_url=('login'))
def createPost(request):
    form= NewPostForm()
    if request.method=='POST':
        form=NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            print(request.user.id)
            profile=Profile.objects.get(user=request.user.id)

            post.profile=profile
            post.save()
            return redirect('home')

        print('not valid')
    context = {'form':form}
    return render(request,'base/post_form.html',context)