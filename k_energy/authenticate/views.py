
from django.shortcuts import render, redirect
from .forms import StepOne, StepTwo
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# 1ere etape
def register_step_one(request):
    if request.method == 'POST':
        form = StepOne(request.POST)
        if form.is_valid():
            request.session['user_info'] = form.cleaned_data  # stock temporaire
            return redirect('inscription2')
    else:
        form = StepOne()
    return render(request, 'inscription.html', {'form': form})

# 2eme etape
def register_step_two(request):
    user_info = request.session.get('user_info')
    if not user_info:
        return redirect('step_one')

    if request.method == 'POST':
        form = StepTwo(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=user_info['email'],
                email=user_info['email'],
                first_name=user_info['first_name'],
                last_name=user_info['last_name'],
                password=password
            )
            messages.success(request, "Inscription réussie !")
            return redirect('connexion')
    else:
        form = StepTwo()
    return render(request, 'inscription2.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('accueil')  # a remplacer par la page d'accueil
        else:
            messages.error(request, 'Adresse email ou mot de passe incorrect.')

    return render(request, 'connexion.html')

def logout_view(request):
    logout(request)
    return redirect('connexion')