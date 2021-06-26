from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.base import TemplateView 
from manuais.forms import EquipamentosForm, RevisaomanualForm
from manuais.models import Equipamentos, RevisaoManuais


# --- equipamentos views --- #
class EquipamentosIndexView(TemplateView):
	template_name = 'equipamento/index-equipamentos.html'


class EquipamentosNewView(CreateView):
	template_name = 'equipamento/equipamento-novo.html'
	form_class = EquipamentosForm
	success_url = reverse_lazy('equipamentos')
	success_message = 'Equipamento Cadastrado com sucesso'


class EquipamentosDeleteView(DeleteView):
	model = Equipamentos
	template_name = 'equipamento/equipamento-delete.html'
	success_url = reverse_lazy('equipamentos')
	success_message = 'O equipamento foi deletado com sucesso'


class EquipamentosUpdateView(UpdateView):
	model = Equipamentos
	form_class = EquipamentosForm
	template_name = 'equipamento/equipamento-alterar.html'
	success_url = reverse_lazy('equipamentos')
	success_message = 'As alterações foram efectuadas com sucesso'


class EquipamentosListView(ListView):
	model = Equipamentos
	template_name = 'equipamento/equipamentos.html'


# --- manuais views --- #
class ManuaisIndexView(TemplateView):
	template_name = 'manuais/index-manuais.html'


class ManuaisNewView(CreateView):
	template_name = 'manuais/manual-novo.html'
	form_class = RevisaomanualForm
	model = RevisaoManuais
	
	def get(self, request, *args, **kwargs):     
		form = RevisaomanualForm()
		equipamento = Equipamentos.objects.values_list().filter(pk=kwargs['pk']) 
		context = {
			'form': form,
			'equipamento': equipamento
		}
		return render(request, 'manuais/manual-novo.html', context)

	def post(self, request, *args, **kwargs):
		equipamento_pk = kwargs['pk']
		equipamento = Equipamentos.objects.filter(pk=equipamento_pk)
		form = self.get_form()

		print(equipamento)
		print(equipamento[0])

		if 'btn_adicionar' in self.request.POST: 

			if form.is_valid():
				form_model = form.save(commit=False)
				form_model.nome_equipamento = equipamento[0]
				form_model.save() 
				return self.form_valid(form)

			else:
				return self.form_invalid(form) 

	def get_success_url(self) -> str:
		messages.success(self.request, 'O manual foi Cadastrado com sucesso')
		return reverse_lazy('equipamentos')


class ManuaisDeleteView(DeleteView):
	model = RevisaoManuais  
	template_name = 'manuais/manual-delete.html' 

	def get_success_url(self):
		messages.success(self.request,'O manual foi deletado com sucesso')
		return reverse_lazy('manuais', kwargs = {'pk': self.object.nome_equipamento.id })


class ManuaisUpdateView(UpdateView):
	model = RevisaoManuais
	form_class = RevisaomanualForm
	template_name = 'manuais/manual-alterar.html' 

	def get_success_url(self) -> str:
		messages.success(self.request, 'Manual Cadastrado com sucesso')
		return reverse_lazy('equipamentos') 

class ManuaisListView(ListView):
	model = RevisaoManuais
	template_name = 'manuais/manuais.html'
	context_object_name = 'manuais_list'

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		equipamentos = Equipamentos.objects.filter(pk=kwargs['pk'])

		context = {
			'pk': kwargs['pk'],
			'manuais': RevisaoManuais.objects.filter(nome_equipamento=kwargs['pk']),
			'obg_equipamento': equipamentos
		}

		# return render(request, self.template_name, context)
		return self.render_to_response(context)

	def get_queryset(self):

		return RevisaoManuais.objects.filter(nome_equipamento_id=self.kwargs['pk'])
