import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(request, password, confirm_password):

    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False

    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False

    return True


def null_fields_is_valid(request, username, email, password):

    if username.strip() == '':
        messages.add_message(request, constants.ERROR, 'O usuário não pode ser vazio')
        return False
    
    if email.strip() == '':
        messages.add_message(request, constants.ERROR, 'O email não pode ser vazio')
        return False

    if password.strip() == '':
        messages.add_message(request, constants.ERROR, 'A senha não pode ser vazia')
        return False
    
    return True