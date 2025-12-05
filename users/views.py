from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/profile.html', {'user': user})

