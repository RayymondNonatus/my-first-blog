from django.contrib import admin
from django.contrib import admin
from .models import Cliente
from .models import Funcionario
from .models import Venda

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Venda)

# Register your models here.
