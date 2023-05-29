from django.urls import path
# Importa as views que a gente criou
from .views import ResponsaveisTecnicosCreate, ProdutorRuralCreate, PropriedadeCreate, DiagnosticoCreate
from .views import ResponsaveisTecnicosUpdate, ProdutorRuralUpdate, PropriedadeUpdate, DiagnosticoUpdate
from .views import ResponsaveisTecnicosDelete, ProdutorRuralDelete, PropriedadeDelete, DiagnosticoDelete
from .views import ResponsaveisTecnicosList, ProdutorRuralList, PropriedadeList, DiagnosticoList
from .views import ResponsaveisDetailView, ProdutorRuraDetailView, PropriedadeDetailView, DiagnosticoDetailView

# Tem que ser urlpatterns porque é o padrão do django
urlpatterns = [
    path('cadastrar/tecnico/', ResponsaveisTecnicosCreate.as_view(), name="cadastrar-tecnico"),
    path('cadastrar/produtor/', ProdutorRuralCreate.as_view(), name="cadastrar-produtor"),
    path('cadastrar/propriedade/', PropriedadeCreate.as_view(), name="cadastrar-propriedade"),
    path('cadastrar/diagnostico/', DiagnosticoCreate.as_view(), name="cadastrar-diagnostico"),

    path('editar/tecnico/<int:pk>/', ResponsaveisTecnicosUpdate.as_view(), name="editar-tecnico"),
    path('editar/produtor/<int:pk>/', ProdutorRuralUpdate.as_view(), name="editar-produtor"),
    path('editar/propriedade/<int:pk>/', PropriedadeUpdate.as_view(), name="editar-propriedade"),
    path('editar/diagnostico/<int:pk>/', DiagnosticoUpdate.as_view(), name="editar-diagnostico"),

    path('excluir/tecnico/<int:pk>/', ResponsaveisTecnicosDelete.as_view(), name="excluir-tecnico"),
    path('excluir/produtor/<int:pk>/', ProdutorRuralDelete.as_view(), name="excluir-produtor"),
    path('excluir/propriedade/<int:pk>/', PropriedadeDelete.as_view(), name="excluir-propriedade"),
    path('excluir/diagnostico/<int:pk>/', DiagnosticoDelete.as_view(), name="excluir-diagnostico"),

    path('listar/tecnico/', ResponsaveisTecnicosList.as_view(), name="listar-tecnico"),
    path('listar/produtor/', ProdutorRuralList.as_view(), name="listar-produtor"),
    path('listar/propriedade/', PropriedadeList.as_view(), name="listar-propriedade"),
    path('listar/diagnostico/', DiagnosticoList.as_view(), name="listar-diagnostico"),

    path('responsaveis/<int:pk>/', ResponsaveisDetailView.as_view(), name="detail-tecnico"),
    path('produtor/<int:pk>/', ProdutorRuraDetailView.as_view(), name="detail-produtor"),
    path('propriedade/<int:pk>/', PropriedadeDetailView.as_view(), name="detail-propriedade"),
    path('diagnostico/<int:pk>/', DiagnosticoDetailView.as_view(), name="detail-Diagnostico"),
]