from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as error404
from .models import livros,usuarios,editoras,categorias
from django.http import HttpResponse
from . import urls
from django.contrib.auth import logout

def viewsAdmIndex(request):
	try:
		dbusuarios=usuarios.objects.all()
		dblivros=livros.objects.all()
		return render(request,'helloAdm.html',{'usuarios':dbusuarios,'livros':dblivros})
	except:
		return HttpResponse("Ocorreu um erro ao renderizar 'helloAdm.html' ")

def tap(request):
	try:
		dbusuarios=usuarios.objects.all()
		dblivros=livros.objects.all()
		return render(request,'helloAdm.html',{'usuarios':dbusuarios,'livros':dblivros})
	except:
		return HttpResponse("Ocorreu um erro ao renderizar 'helloAdm.html' ")



#Funções/Métodos do um usuário: ---------------------------------------------------------------
#leva até a tela de login
def viewsindex(request):
	return render(request,'index.html')

#leva até a tela de registro
def viewstregistro(request):
	return render(request,'tregistro.html')

#leva até pág tperfil
def viewstperfil(request,id):
	usuario=error404(usuarios,pk=id)
	return render(request,'tperfil.html',{'usuario':usuario})

def viewstverlivro(request,id,id2):
	try:
		bdlivros=error404(livros,pk=id)
		dbusuarios=error404(usuarios,pk=id2)
		return render(request,'tverlivro.html',{'livro':bdlivros,'usuario':dbusuarios})
	except:
		dbusuarios=error404(usuarios,pk=id)
		return render(request,'tverlivro.html',{'usuario':dbusuarios,'VerAlert':"Ocorreu um erro ao renderizar Prateleira"})

#leva até pág tprateleira
def viewstprateleira(request,id):
	try:
		usuario=error404(usuarios,pk=id)
		allLivros=livros.objects.all()
		return render(request,'tprateleira.html',{'usuario':usuario,'bdlivros':allLivros})
	except:
		usuario=error404(usuarios,pk=id)
		return render(request,'tperfil.html',{'usuario':usuario, 'LivrariaAlert':"Ocorreu um erro ao renderizar Prateleira"})


def defbtnlogin(request):
	if request.method=="POST":
		email=request.POST.get('email')
		senha=request.POST.get('senha')
		try:
			buscaUsuario=error404(usuarios,email=email)
		except:
			#matendo email e senha até o usuário lembrar
			return render(request,'index.html',{'EmailAlert':"Email não encontrado",'kepEmail':email,'kepSenha':senha})
		
		if buscaUsuario.senha==senha:
			return render(request,'tperfil.html',{'usuario':buscaUsuario})

		else:
			#matendo email até o usuário lembrar a senha
			return render(request,'index.html',{'SenhaAlert':"Senha errada",'kepEmail':email})

def defbtnregistro(request):
	if request.method=="POST":
		email=request.POST.get('email')
		buscaEmails=usuarios.objects.filter(email=email)
		if not buscaEmails:
			email=request.POST.get('email')
			nome=request.POST.get('nome')
			sobrenome=request.POST.get('sobrenome')
			senha=request.POST.get('senha')
			addUsuario=usuarios(nome=nome,sobrenome=sobrenome,senha=senha,email=email)
			addUsuario.save()
			#levando mantendo os dados e levando para a página de login para entrar no app
			return render(request,'index.html',{'kepEmail':email,'kepSenha':senha})
		else:
			email=request.POST.get('email')
			senha=request.POST.get('senha')
			nome=request.POST.get('nome')
			sobrenome=request.POST.get('sobrenome')
			return render(request,'tregistro.html',{'EmailAlert':"Email já Cadastrado",'kepNome':nome,'kepSobrenome':sobrenome,'kepSenha':senha,'kepEmail':email,})

def defbtndelete(request,id):
	try:
		user=error404(usuarios,pk=id)
		user.delete()
		try:
			return render(request,'index.html')
		except:
			return render(request,'index.html')
	except:
		return render(request,'tperfil.html',{'usuario':usuario,'UserAlert':"Usuario não encontrado"})

def defbtneditar(request,id):
	if request.method=="POST":
		try:
			usuario=error404(usuarios,pk=id)
			usuario.email=request.POST.get('email')
			usuario.nome=request.POST.get('nome')
			usuario.sobrenome=request.POST.get('sobrenome')
			usuario.senha=request.POST.get('senha')
			usuario.save()
			return render(request,'tperfil.html',{'usuario':usuario})
		except:
			return render(request,'tperfil.html',{'usuario':usuario,'UserAlert':"Usuario não encontrado"})

		
