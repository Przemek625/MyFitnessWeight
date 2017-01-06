from django.shortcuts import render, redirect
from login.forms import LoginForm
from django.contrib.auth import login, authenticate


def process_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_user_email = form.cleaned_data['email']
            form_user_password = form.cleaned_data['password']
            user = authenticate(username=form_user_email, password=form_user_password)
            if user is not None:
                login(request, user=user)
                redirect('login_success.html')
            else:
                form.add_error(None, 'Invalid Username of Password')
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
