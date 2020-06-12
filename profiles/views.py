from django.shortcuts import render

from .models import Profile


def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    print('profile', profile.user.username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
