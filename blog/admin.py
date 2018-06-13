from django.contrib import admin
from .models import Jogador
from .models import Time
from .models import Time_Jogador
'''from .models import Jogo'''

admin.site.register(Jogador)
admin.site.register(Time)
admin.site.register(Time_Jogador)
'''admin.site.register(Jogo)'''


