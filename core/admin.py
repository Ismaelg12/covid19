from django.contrib import admin
from core.models import Prefeitura, Bairro, Caso, Comorbidade, Diario, Ubs, Teste, Semana, Media, Conf_mes, Obitos_mes

class PrefeituraAdmin(admin.ModelAdmin):
	list_display = ['orgao','cidade','secretaria','coordenacao'] 

class CasoAdmin(admin.ModelAdmin):
	list_display = ['nome','bairro','confirmado','recuperado','isolado',
	'obito','comorbidade','sexo'] 
	search_fields  = ['nome','bairro',]

class BairroAdmin(admin.ModelAdmin):
	list_display = ['nome','cidade','latitude', 'longitude'] 
	search_fields  = ['nome']

class ComorbidadeAdmin(admin.ModelAdmin):
	list_display = ['id','tipo'] 
	search_fields  = ['tipo']

class DiarioAdmin(admin.ModelAdmin):
	list_display = ['id','confirmado','recuperado', 'obito','criado_em', 'conf_por_dia','obt_por_dia'] 
	
class UbsAdmin(admin.ModelAdmin):
	list_display = ['id','nome']
	search_fields  = ['nome'] 

class TesteAdmin(admin.ModelAdmin):
	list_display = ['id','total','descartado']

class SemanaAdmin(admin.ModelAdmin):
	list_display = ['id','semana','conf_sm','obt_sm','trans_sm']

class MediaAdmin(admin.ModelAdmin):
	list_display = ['id','media_dia','media_conf','tx_conf','media_obt', 'tx_obt']

class Conf_mesAdmin(admin.ModelAdmin):
	list_display = ['id','conf_mes','total_conf_mes','media_conf_mes','status_conf_mes','criado_em']

class Obitos_mesAdmin(admin.ModelAdmin):
	list_display = ['id','obitos_mes','total_obitos_mes','media_obitos_mes','status_obitos_mes','criado_em']

admin.site.register(Prefeitura,PrefeituraAdmin)
admin.site.register(Bairro,BairroAdmin)
admin.site.register(Caso,CasoAdmin)
admin.site.register(Comorbidade,ComorbidadeAdmin)
admin.site.register(Diario,DiarioAdmin)
admin.site.register(Ubs,UbsAdmin)
admin.site.register(Teste,TesteAdmin)
admin.site.register(Semana,SemanaAdmin)
admin.site.register(Media,MediaAdmin)
admin.site.register(Conf_mes,Conf_mesAdmin)
admin.site.register(Obitos_mes,Obitos_mesAdmin)