from django.http import Http404
from django.shortcuts import render, redirect

from registration.forms import RegistrationForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['register_successfully'] = True
            return redirect('success_registration')
        else:
            render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def success_registration(request):
    if request.session['register_successfully']:
        del request.session['register_successfully']
        return render(request, 'success_registration.html')
    else:
        raise Http404('This page is not available for you')