from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import CustomUserCreationForm, UserUpdateForm  # Добавлена форма для обновления
from users.models import Support, UserProduct


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


@login_required
def user_profile(request):
	user = request.user

	if request.method == 'POST':
		form = UserUpdateForm(request.POST, request.FILES, instance=request.user)  # Используем новую форму
		if form.is_valid():
			form.save()
			return redirect('user_profile')
	else:
		form = UserUpdateForm(instance=request.user)  # Используем новую форму

	user_products = UserProduct.objects.filter(user=request.user)
	return render(request, 'users/user_profile.html', {
		'user': user,
		'form': form,
		'user_products': user_products,
	})


def support_view(request):
	if request.method == 'POST':
		mail = request.POST.get('recipient-name')
		text = request.POST.get('message-text')

		Support.objects.create(mail=mail, text=text)

	return render(request, 'sell/support.html')