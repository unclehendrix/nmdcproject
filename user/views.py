from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UpdateUserForm,ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context={
        'form':form
    }
    return render(request,'user/register.html', context )

def profile(request):
    return render (request,'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST,instance=request.user)
        profileform = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('user-profile')
    else:
        userform = UpdateUserForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)
    context={
        'user_form': userform,
        'profile_form':profileform
    }
    return render(request,'user/profile_update.html',context)