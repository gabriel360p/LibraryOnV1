from django.db import models

class usuarios(models.Model):
	nome=models.CharField(max_length=50)
	sobrenome=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	senha=models.CharField(max_length=50)

	def __str__(self):
		return f'{self.nome},{self.sobrenome},{self.email},{self.senha}'

class categorias(models.Model):
	nome=models.CharField(max_length=120)
	subcategoria=models.CharField(max_length=120)
	
	def __str__(self):
		return f'{self.nome},{self.subcategoria}'


class editoras(models.Model):
	nome=models.CharField(max_length=120)
	
	def __str__(self):
		return f'{self.nome}'


class livros(models.Model):
	titulo=models.CharField(max_length=50)
	autor=models.CharField(max_length=50)
	preco=models.FloatField()
	estoque=models.IntegerField()
	publicacao=models.DateField()
	descricao=models.TextField()
	categoria=models.ForeignKey(categorias,on_delete=models.CASCADE)
	editora=models.ForeignKey(editoras,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.titulo},{self.autor},{self.preco},{self.publicacao},{self.categoria},{self.editora},{self.descricao}'



