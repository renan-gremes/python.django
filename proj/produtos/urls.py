#Request > urls > views > model > responde
# 1 - Request do navegador
# 2 - Urls dos arquivos urls.py
# 3 - Views (progra em si) do arquivo view.py do projeto (produtos, proj, etc)
# 4 - Model são os dados do banco
# 5 - Response é o retorno da função (view)

from django.urls import path
from .views import home, produto


urlpatterns = [
    path('', home), #Se não digitar nada a home de views irá ser devolvida 
    path('produto/<int:codigo>/', produto), #view produto sendo devolvida na url do primeiro parâmetro
]