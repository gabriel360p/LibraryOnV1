from django.urls import path
from . import views

app_name="livraria"

urlpatterns=[
	#Rotas de um adm/superusuário: ---------------------------------------------------------------
	#rota index do adm
	path('',views.viewsAdmIndex,name="admindex"),
	path('tap/',views.tap,name="tap"),
	# ---------------------------------------------------------------



	#Rotas de um usuário: ---------------------------------------------------------------
	#rota index do usuario. Leva até a tela de login
	path('index/',views.viewsindex,name="index"),
	#rota até a pág perfil do usuario.
	path('tperfil/<int:id>',views.viewstperfil,name="tperfil"),
	#rota até a pág livraria.
	path('tprateleira/<int:id>',views.viewstprateleira,name="tprateleira"),
	#rota até a pág ver conteúdo do livro
	path('tverlivro/<int:id> <int:id2>',views.viewstverlivro,name="tverlivro"),
	

	#leva até a tela de registro
	path('tregistro/',views.viewstregistro,name="tregistro"),
	#url do botão que faz o login
	path('defbtnlogin/',views.defbtnlogin,name="defbtnlogin"),
	#url do botão que faz o registro de usuários
	path('defbtnregistro/',views.defbtnregistro,name="defbtnregistro"),
	#url do botão que faz deleta o perfil do usuário
	path('defbtndelete/<int:id>',views.defbtndelete,name="defbtndelete"),
	#url do botão que salva a edição dos dados do usuário
	path('defbtneditar/<int:id>',views.defbtneditar,name="defbtneditar"),
	# ---------------------------------------------------------------
]




