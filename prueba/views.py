# Create your views here.

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Persona, Mascota

# Vistas para Persona
class PersonaListView(LoginRequiredMixin, ListView):
    model = Persona
    template_name = 'Templates/persona_list.html'

class PersonaCreateView(PermissionRequiredMixin, CreateView):
    model = Persona
    template_name = 'Templates/persona_form.html'
    fields = ['cedula', 'nombres', 'apellidos', 'genero']
    permission_required = 'prueba.add_persona'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(PermissionRequiredMixin, UpdateView):
    model = Persona
    template_name = 'Templates/persona_form.html'
    fields = ['cedula', 'nombres', 'apellidos', 'genero']
    permission_required = 'prueba.change_persona'
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Persona
    template_name = 'Templates/persona_confirm_delete.html'
    success_url = reverse_lazy('persona_list')
    permission_required = 'prueba.delete_persona'

# Vistas para Mascota
class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'Templates/mascota_list.html'

class MascotaCreateView(PermissionRequiredMixin, CreateView):
    model = Mascota
    template_name = 'Templates/mascota_form.html'
    fields = ['nombre', 'raza', 'genero', 'cedula']
    permission_required = 'prueba.add_mascota'
    success_url = reverse_lazy('mascota_list')

class MascotaUpdateView(PermissionRequiredMixin, UpdateView):
    model = Mascota
    template_name = 'Templates/mascota_form.html'
    fields = ['nombre', 'raza', 'genero', 'cedula']
    permission_required = 'prueba.change_mascota'
    success_url = reverse_lazy('mascota_list')

class MascotaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'Templates/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_list')
    permission_required = 'prueba.delete_mascota'
