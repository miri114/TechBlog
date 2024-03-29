from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from . forms import SignUpForm, EditProfileForm, PasswordsChangeForm, UserProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from  blog.models import UserProfile

class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name="registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name="registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name="registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = "registration/edit_profile_page.html"
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url','twitter_url','instagram_url', 'github_url', 'linkedin_url',]



class CreateProfilePageView(generic.CreateView):
    model = UserProfile
    form_class = UserProfilePageForm
    template_name =  'registration/create_user_profile_page.html'
    # fields = '__all__'     # since we creating new profile, this takes all fields of a userprofile defined in models.py

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    