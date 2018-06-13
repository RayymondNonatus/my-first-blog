from django.db import models
from django.utils import timezone

class Jogador(models.Model):
    Nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11)
    Data_de_Nascimento = models.DateField()
    Email = models.EmailField()
    Nacionalidade = models.CharField(max_length=15)
    Titulos = models.IntegerField()

    def __str__(self):
        return self.Nome

class Time(models.Model):
    Razão_Social = models.CharField(max_length=50)
    '''Mascote = models.ImageField()'''
    CNPJ = models.CharField(max_length=14)
    Email = models.EmailField()

    def __str__(self):
        return self.Razão_Social
    
class Time_Jogador(models.Model):
    Time = models.ForeignKey('Time', on_delete=models.CASCADE)
    Jogador = models.ForeignKey('Jogador', on_delete=models.PROTECT)
    Inicio_do_Contrato = models.DateField()
    Termino_do_Contrato = models.DateField()

'''class Jogo(models.Model):
    Time_1 = models.ForeignKey('Time', on_delete=models.CASCADE)
    Time_2 = models.ForeignKey('Time', on_delete=models.CASCADE)
    Data = models.DateTimeField()
    Resultado = models.CharField(max_length=5)'''
    
    
    





