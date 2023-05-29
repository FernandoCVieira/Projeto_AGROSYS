from django.contrib import admin
# Importar as classes
from .models import ResponsaveisTecnicos, ProdutorRural, Propriedade, Diagnostico

# Register your models here.
admin.site.register(ResponsaveisTecnicos)
admin.site.register(ProdutorRural)
admin.site.register(Propriedade)
admin.site.register(Diagnostico)