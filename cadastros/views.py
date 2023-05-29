from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import ResponsaveisTecnicos, ProdutorRural, Propriedade, Diagnostico
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from django.urls import reverse
#from braces.views import GroupRequiredMixin
#from django.shortcuts import get_object_or_404

# Create your views here.
class ResponsaveisTecnicosCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = ResponsaveisTecnicos
    fields = ['usuario', 'nome_tecnico', 'cnpj_tecnico', 'numero_registro', 'produtores_rurais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tecnico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Responsaveis Tecnicos"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
    
        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class ProdutorRuralCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    #group_required = u"Tecnico"
    model = ProdutorRural
    fields = ['nome_rural', 'propriedade_local', 'responsaveis_tecnicos']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro do Produtor Rural"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
class PropriedadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Propriedade
    fields = ['produtor_rural', 'descricao', 'cnpj_propriedade', 'local', 'latitude', 'longitude']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-propriedade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro Propriedade"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
class DiagnosticoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Diagnostico
    fields = ['propriedade', 'cultura', 'produto_comercial', 'alvo', 'area_a_tratar',
              'volume_da_calda', 'intervalo_de_seguranca', 'modalidade_aplicacao',
              'equipamento_aplicacao', 'quantidade_a_adquirir', 'n_aplicacoes', 'epoca_aplicacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-diagnostico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro Propriedade"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
################## UPDATE ##################

class ResponsaveisTecnicosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = ResponsaveisTecnicos
    fields = ['usuario', 'nome_tecnico', 'cnpj_tecnico', 'numero_registro', 'produtores_rurais']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tecnico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Responsaveis Tecnicos"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
class ProdutorRuralUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    #group_required = u"Tecnico"
    model = ProdutorRural
    fields = ['nome_rural', 'propriedade_local', 'responsaveis_tecnicos']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Produtor Rural"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class PropriedadeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Propriedade
    fields = ['produtor_rural', 'descricao', 'cnpj_propriedade', 'local', 'latitude', 'longitude']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-propriedade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Propriedade"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class DiagnosticoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Diagnostico
    fields = ['propriedade', 'cultura', 'produto_comercial', 'alvo', 'area_a_tratar',
              'volume_da_calda', 'intervalo_de_seguranca', 'modalidade_aplicacao',
              'equipamento_aplicacao', 'quantidade_a_adquirir', 'n_aplicacoes', 'epoca_aplicacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-diagnostico')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Propriedade"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

################## DELETE ##################

class ResponsaveisTecnicosDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = ResponsaveisTecnicos
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-tecnico')

class ProdutorRuralDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    #group_required = u"Tecnico"
    model = ProdutorRural
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtor')

class PropriedadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Propriedade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-propriedade')

class DiagnosticoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Diagnostico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-diagnostico')

################## LISTA ##################

class ResponsaveisTecnicosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ResponsaveisTecnicos
    template_name = 'cadastros/listas/tecnicos.html'

class ProdutorRuralList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ProdutorRural
    template_name = 'cadastros/listas/produtor.html'

class PropriedadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Propriedade
    template_name = 'cadastros/listas/propriedade.html'

class DiagnosticoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Diagnostico
    template_name = 'cadastros/listas/diagnostico.html'

################## DETAILVIEW ##################

class ResponsaveisDetailView(DetailView):
    model = ResponsaveisTecnicos
    template_name = 'cadastros/print.html'

class PropriedadeDetailView(DetailView):
    model = Propriedade
    template_name = 'cadastros/print.html'
    
class ProdutorRuraDetailView(DetailView):
    model = ProdutorRural
    template_name = 'cadastros/print.html'

class DiagnosticoDetailView(DetailView):
    model = Diagnostico
    template_name = 'cadastros/print.html'