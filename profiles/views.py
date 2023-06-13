from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile

# Create your views here.


def register(request):
    # Handle user registration

    # Create profile for the registered user
    profile = UserProfile(user=user)
    profile.save()

    # Redirect to the profile page
    return redirect('profile')


@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    context = {
        'user': request.user,
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)