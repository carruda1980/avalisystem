from django.contrib import admin
from .models import Produto, Voto

class ProdutoAdmin(admin.ModelAdmin):
    pass

class VotoAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Voto, VotoAdmin)
