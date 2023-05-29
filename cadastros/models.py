from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Método e Choices

def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)

class ResponsaveisTecnicos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    nome_tecnico = models.CharField(max_length=50, verbose_name="Nome")
    cnpj_tecnico = models.CharField(max_length=14, verbose_name="CNPJ")
    numero_registro = models.CharField(max_length=20, verbose_name="Número CREA/CFTA")
    produtores_rurais = models.ManyToManyField("ProdutorRural", verbose_name="Produtor Rural", blank=True)

    def __str__(self):
        return "{} ({})".format(self.nome_tecnico, self.numero_registro)
    
class ProdutorRural(models.Model):
    nome_rural = models.CharField(max_length=50, verbose_name="Nome")
    propriedade_local = models.CharField(max_length=100, verbose_name="Propriedade")
    responsaveis_tecnicos = models.ManyToManyField(ResponsaveisTecnicos, verbose_name="Responsáveis Técnicos")

    def __str__(self):
        return "{} ({}) -> {}".format(self.nome_rural, self.propriedade_local, self.responsaveis_tecnicos)

class Propriedade(models.Model):
    produtor_rural = models.ForeignKey(ProdutorRural, on_delete=models.PROTECT, verbose_name="Produtor Rural")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    cnpj_propriedade = models.CharField(max_length=14, verbose_name="CNPJ")
    local = models.CharField(max_length=100, verbose_name="Local")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.produtor_rural, self.descricao, self.cnpj_propriedade, self.local, self.latitude, self.longitude)
    
class Diagnostico(models.Model):
    propriedade = models.ForeignKey(Propriedade, on_delete=models.PROTECT)
    cultura = models.CharField(max_length=100, verbose_name="Cultura")
    produto_comercial = models.CharField(max_length=100, verbose_name="Produto Comercial")
    alvo = models.CharField(max_length=100, verbose_name="Alvo")
    area_a_tratar = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Área a tratar")
    volume_da_calda = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Volume de calda")
    intervalo_de_seguranca = models.IntegerField(verbose_name="Intervalo de segurança")
    modalidade_aplicacao = models.CharField(max_length=100, verbose_name="Modalidade de aplicação")
    equipamento_aplicacao = models.CharField(max_length=100, verbose_name="Equipamento de aplicação")
    quantidade_a_adquirir = models.IntegerField(verbose_name="Quantidade a adquirir")
    n_aplicacoes = models.IntegerField(verbose_name="Nº aplicação")
    epoca_aplicacao = models.CharField(max_length=100, verbose_name="Época de aplicação")

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {}".format(self.propriedade, self.cultura, self.produto_comercial, self.alvo,
                                                            self.area_a_tratar, self.volume_da_calda, self.intervalo_de_seguranca,
                                                            self.modalidade_aplicacao, self.equipamento_aplicacao, self.quantidade_a_adquirir,
                                                            self.n_aplicacoes, self.epoca_aplicacao)