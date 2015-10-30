from django.shortcuts import render_to_response
from apps.usuarios.form import  RegistrarUsuario
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render


def registrar(request):
    if request.POST:
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = RegistrarUsuario()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('usuarios_templates/registrar_usuario.html', args)

def login(request): 
    return render(request,'usuarios_templates/login.html') 