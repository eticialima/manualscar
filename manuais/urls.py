from django.urls import path, re_path 
from manuais.views import (EquipamentosDeleteView, EquipamentosListView, EquipamentosNewView,
                           EquipamentosUpdateView, ManuaisDeleteView, ManuaisListView, ManuaisNewView, ManuaisUpdateView)

# app_name = "equipment" 
urlpatterns = [ 
	path('equipamentos/', EquipamentosListView.as_view(), name='equipamentos'), 
	path('Equipamento-novo/', EquipamentosNewView.as_view(), name='equipoamento-novo'),
	path('<int:pk>/alterar/', EquipamentosUpdateView.as_view(), name='equipamento-alterar'),
	path('<int:pk>/delete/', EquipamentosDeleteView.as_view(), name='equipamento-delete'), 
 
	path('equipamentos/<int:pk>/', ManuaisListView.as_view(), name='manuais'), 
	path('<str:pk>/manual-novo/', ManuaisNewView.as_view(), name='manual-novo'),
	path('alterar/<int:pk>/', ManuaisUpdateView.as_view(), name='manual-alterar'),
	path('delete/<int:pk>', ManuaisDeleteView.as_view(), name='manual-delete'),  
]
