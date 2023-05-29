from django.urls import path
# Importa as views que a gente criou
from .views import IndexView, SobreView

# Tem que ser urlpatterns porque é o padrão do django
urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]