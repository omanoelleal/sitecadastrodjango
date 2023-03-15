from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def ver_user(request):
    usuarios = {
    'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

def usuarios(request):
    #Salvar os dados do novo usuário
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    return redirect('ver_user')

