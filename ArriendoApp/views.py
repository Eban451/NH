from django.shortcuts import render, redirect
from .forms import UsuarioRegisterForm, DireccionForm, PropiedadForm, UsuarioUpdateForm
from .decorators import user_is_arrendador
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

####

def register(request):
    if request.method == 'POST':
        user_form = UsuarioRegisterForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        if user_form.is_valid() and direccion_form.is_valid():
            direccion = direccion_form.save()
            user = user_form.save(commit=False)
            user.direccion = direccion
            user.save()
            return redirect('home')
    else:
        user_form = UsuarioRegisterForm()
        direccion_form = DireccionForm()
    return render(request, 'registration/register.html', {'user_form': user_form, 'direccion_form': direccion_form})

@user_is_arrendador
def create_propiedad(request):
    if request.method == 'POST':
        propiedad_form = PropiedadForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        if propiedad_form.is_valid() and direccion_form.is_valid():
            direccion = direccion_form.save()
            propiedad = propiedad_form.save(commit=False)
            propiedad.direccion = direccion
            propiedad.arrendador = request.user
            propiedad.save()
            return redirect('home')
    else:
        propiedad_form = PropiedadForm()
        direccion_form = DireccionForm()
    return render(request, 'registration/create-propiedad.html', {'propiedad_form': propiedad_form, 'direccion_form': direccion_form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UsuarioUpdateForm(request.POST, instance=request.user)
        direccion_form = DireccionForm(request.POST, instance=request.user.direccion)
        
        if user_form.is_valid() and direccion_form.is_valid():
            direccion = direccion_form.save()
            user = user_form.save(commit=False)
            user.direccion = direccion
            user.save()
            return redirect('profile')
    else:
        user_form = UsuarioUpdateForm(instance=request.user)
        direccion_form = DireccionForm(instance=request.user.direccion)

    return render(request, 'profile.html', {'user_form': user_form, 'direccion_form': direccion_form})

