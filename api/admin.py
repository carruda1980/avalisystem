# Third
from django.contrib import admin

# Local
from .models import Produto, Voto


class VotoInLine(admin.TabularInline):
    model = Voto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'cadatrado_em', 'produto_nome_maiusculo', 'slug')
    prepopulated_fields = {"slug": ("produto",)}
    search_fields = ['produto', 'slug']
    inlines = [VotoInLine]

    def produto_nome_maiusculo(self, obj):
        return ("%s" % (obj.produto)).upper()
    produto_nome_maiusculo.short_description = 'Nome do produto'


class VotoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'nota', 'cadatrado_em', 'ponto_positivo', 'ponto_negativo',)
    list_filter = ('produto', 'cadatrado_em',)
    raw_id_fields = ("produto",)
    search_fields = ['produto__produto']


# Registrando os Models
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Voto, VotoAdmin)
