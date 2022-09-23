from django.shortcuts import render, redirect
from YasCatálogo.forms import UsersForm
from YasCatálogo.models import Users

# Create your views here.

def home(request):
    tabela= Users.objects.all()
    return render(request, 'home.html', {'usuario': tabela})
    
def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def docad(request):
    tabela= Users.objects.all()
    form = UsersForm (request.POST or None)
    erro = ''
    for c in tabela:
        if form ['usuario'].data == c.usuario:
            erro= ("mensagem de erro")
    if form.is_valid() and erro== '':
        form.save()
    return redirect('cadastro')
 