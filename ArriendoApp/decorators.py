from django.shortcuts import redirect

def user_is_arrendador(function):
    def wrap(request, *args, **kwargs):
        if request.user.tipo_usuario_id == 1:  # Verifica si el usuario es un arrendador
            return function(request, *args, **kwargs)
        else:
            return redirect('home')  # Redirige al index si no es un arrendador
    return wrap
