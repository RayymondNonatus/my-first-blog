from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    
    nome_cliente = models.CharField(max_length=200)
    created_date = models.DateField()
    def __str__(self):
        return self.nome_cliente
    

class Funcionario(models.Model):
    
    nome_func = models.CharField(max_length=200)
    created_date = models.DateField()
    def __str__(self):
        return self.nome_func
    
class Venda(models.Model):
    
   nome_func = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
   nome_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
   


# Create your models here.
