from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid, null_fields_is_valid
from django.shortcuts import redirect

def cadastro(request):

    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not password_is_valid(request, senha, confirmar_senha):
            print('invalid password')
            return redirect('/auth/cadastro')
        
        if not null_fields_is_valid(request, username, email, senha):
            print('invalid null fields')
            return redirect('/auth/cadastro')

        return HttpResponse('teste')



    

def logar(request):
    return HttpResponse('Login')
