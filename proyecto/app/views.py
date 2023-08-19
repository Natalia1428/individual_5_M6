from django.shortcuts import redirect, render
from .forms import FormularioRegistroUsuario, UsuarioForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Usuario




def vista_index(request):
    cuentaActiva = False
    if request.user.is_authenticated:
        cuentaActiva = True
        messages.success(request, f'Cuenta activa : {request.user.username}')
    return render(request, 'index.html', { 'cuentaActiva': cuentaActiva }) 

def vista_clientes(request):
    cuentaActiva = False
    if request.user.is_authenticated:
        messages.success(request, f'Cuenta activa : {request.user.username}')
        cuentaActiva = True
    clientes = Usuario.objects.all()


    return render(request, 'clientes.html', {'clientes' : clientes ,'cuentaActiva': cuentaActiva })


def vista_registroCliente(request):
    cuentaActiva = False
    if request.user.is_authenticated:
        messages.success(request, f'Cuenta activa : {request.user.username}')
        cuentaActiva = True
    if request.method == 'POST':
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('clientes')
        
           
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form , 'cuentaActiva': cuentaActiva})


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, f'Sesión finalizada correctamente!')
    return redirect('index')


def vista_login(request):
    cuentaActiva = False
    if request.user.is_authenticated:
        messages.success(request, f'Cuenta activa : {request.user.username}')
        cuentaActiva= True
        return redirect('index', {'cuentaActiva' : cuentaActiva})
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid(): # si el formulario de login es válido.
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user.username}')
                cuentaActiva= True
                return redirect('index')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    
    form = AuthenticationForm()

    # return render(
    #     request=request,
    #     template_name='login.html',
    #     context={'form':form}
    # )
    return render(request, 'login.html', {'form':form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = FormularioRegistroUsuario()
    return render(request, 'registro_usuario.html', {'form':form})

