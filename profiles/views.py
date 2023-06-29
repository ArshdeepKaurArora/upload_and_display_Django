from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import ProfileForm
from .models import UserProfileModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# def store_file(file):
#     with open('temp/image.png', "wb+") as desk:
#         for chunk in file.chunks():
#             desk.write(chunk)

# Create your views here.

# class CreateProfileView(View):
#     """To return profile page"""
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, 'profiles/create_profile.html',{
#             "form": form
#         })
    
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfileModel(user_image=request.FILES['user_image'])
#             profile.save()
#             redirect_path = reverse("createprofile")
#             return HttpResponseRedirect(redirect_path)
#         return render(request, 'profiles/create_profile.html',{
#             "form": submitted_form
#             })


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfileModel
    fields = "__all__"
    success_url = "/profile"

class AllProfilesView(ListView):
    template_name = "profiles/all_profiles.html"
    model = UserProfileModel
    context_object_name = "profiles"
