from django.contrib import admin
from .models import livros,usuarios,editoras,categorias
# Register your models here.

# admin.site.register(usuarios)
# admin.site.register(livros)
# admin.site.register(editoras)
# admin.site.register(categorias)

@admin.register(usuarios)
class usuariosAdmin(admin.ModelAdmin):
	list_display=('nome','sobrenome','email')
	list_filter=('nome',)
	search_fields=('nome','sobrenome','email')
	list_display_links=('nome',)

@admin.register(livros)
class livrosAdmin(admin.ModelAdmin):
	list_display_links=('titulo',)
	list_display=('titulo','id','editora','autor','publicacao','categoria','preco')
	list_editable=('editora','autor','publicacao','categoria','preco')
	list_filter=('editora','autor','publicacao','categoria')
	search_fields=('nome','editora','autor','categoria')

@admin.register(categorias)
class categoriasAdmin(admin.ModelAdmin):
	list_display=('nome','subcategoria')
	list_display_links=('nome','subcategoria')

@admin.register(editoras)
class editorasAdmin(admin.ModelAdmin):
	list_display=('nome',)
	list_display_links=('nome',)

