from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CustomUser, Profile
from django.views.generic import UpdateView, CreateView, DetailView

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form' : form })

class ProfileCreateView(CreateView):
    model = Profile
    template_name = "registration/create_profile.html"
    fields = ["dob", "profile_pic"]
    success_url = reverse_lazy("shop:all_products")

class ProfileUpDateView(UpdateView):
    model = Profile
    template_name = "registration/edit_profile.html"
    fields = ["dob", "profile_pic"]
    success_url = reverse_lazy("shop:all_products")

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"