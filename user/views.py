from django.shortcuts import get_object_or_404, render
from notes.views import my_notes
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from .forms import UserForm,SignInForm
from django.contrib import messages



def about_page(request):
    return render(request, 'user/about.html')

def signup(request):
    if request.method == 'POST':
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            name = form.cleaned_data.get("name")
            email=form.cleaned_data.get('email')
            pswd=form.cleaned_data.get('password')
            image=form.cleaned_data.get('image')
            bio = form.cleaned_data.get('bio')
            user=CustomUser.objects.create(username=username,email=email,password=make_password(pswd),image=image,name=name,bio=bio)
            messages.success(request,'Account Created')
            login(request,user)
            return redirect(reverse('profile',kwargs={'username':username}))
    else:
        form = UserForm(None)
    context={"form":form}
    return render(request,"user\signup.html",context)


def signin(request):
    form=SignInForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        pswd=form.cleaned_data.get("password")
        user = CustomUser.objects.filter(username=username).first()
        if user:
            if check_password(pswd, user.password):
                login(request,user)
                form=SignInForm(None)
                messages.success(request,f'Welcome Back! {username}')
                return redirect(reverse('notes',kwargs={"search":0}))
            else:
                messages.error(request,'Password is not correct')
                return redirect('signin')
        else:
            messages.error(request,'Username not found, please signup first!')
            return redirect('signin')
        
    return render(request,"user\signin.html",{"form":form})

@login_required
def profile(request,username):
    user=get_object_or_404(CustomUser,username=username)
    if username == request.user.username:
        show_button = True
    else:
        show_button = False 
    mynotes = my_notes(user.id)
    context = {"user":user, "show_button":show_button,"mynotes":mynotes}  
    return render(request, "user/profile.html", context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def delete_profile(request,id):
    obj = get_object_or_404(CustomUser,id = id)
    obj.delete()
    return redirect('signin')

def custom_404(request, exception):
    return render(request, '404.html', status=404)