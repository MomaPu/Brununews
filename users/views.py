from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import (CustomUserCreationForm)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} успешно создан!  Теперь вы можете войти.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required(login_url='login')
def user_profile(request):

    user_products = request.user.products.all()

    context = {
        'username': request.user.username,
        'email': request.user.email,
        'user_products': user_products,
    }
    return render(request, 'users/user_profile.html', context)
