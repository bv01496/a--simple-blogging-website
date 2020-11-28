from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import DetailView,UpdateView
from.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
def register(request):
    if request.method== 'POST':
        form = UserRegistrationForm(request.POST)
        context ={'form':form}
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created as {username}')
            return redirect('home')
        else:
            messages.error(request,'incorrect credentials,please re-enter')
    else:
        form = UserRegistrationForm()
        context ={'form':form}
    return render(request,"user/registration.html",context)
class ProfileDetail(LoginRequiredMixin,DetailView):
    model = Profile
class UpdateProfile(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = User
    success_url = '/'
    template_name = 'user/user_form.html'
    last_name = "nananu"
    fields =['username','email','first_name','last_name']
    def test_func(self):
        user = self.get_object()
        if user == self.request.user:
            return True
        return False