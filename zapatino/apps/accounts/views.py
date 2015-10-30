from django.shortcuts import render

from apps.accounts.form import RegistroUserForm


def registro_usuario_view(request):
    if request.method == 'POST':
        form = RegistroUserForm(request.POST, request.FILES)
    else:
        form = RegistroUserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/registro.html', context)