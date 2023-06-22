from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm


def register(request):
    """"Create profile for the registered user """

    user = User.objects.create_user(username='username', password='password')

    profile = UserProfile(user=user)
    profile.save()

    return redirect('profiles:profile')


@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profiles:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'profile.html', context)