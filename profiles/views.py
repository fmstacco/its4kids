from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from blog.models import Post


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
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profiles:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    user_posts = Post.objects.filter(author=request.user)

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'form': form

    }
    return render(request, 'profile.html', context)

    