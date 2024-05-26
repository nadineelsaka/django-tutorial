from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import RegisterForm, SignUpForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.


def register(request):
    # form = UserCreationForm()
    # form = RegisterForm()
    form = SignUpForm()
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        # form = RegisterForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    return render(request, 'register.html', {'form': form})


class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name')
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user
