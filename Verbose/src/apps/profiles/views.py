```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

@login_required
def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def verbose_mode(request):
    profile = Profile.objects.get(user=request.user)
    profile.verbose_mode = not profile.verbose_mode
    profile.save()
    mode = "ON" if profile.verbose_mode else "OFF"
    messages.success(request, f'Verbose mode turned {mode}')
    return redirect('view_profile')
```