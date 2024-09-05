from rest_framework import generics
from .models import Inventory, Inbound, Outbound
from .serializers import InventorySerializer, InboundSerializer, OutboundSerializer
from .forms import UserRegisterForm, OutboundForm, InboundForm, InventoryForm  
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'signup.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            
            login(request, user)
            return redirect('index')

        return render(request, 'signup.html', {'form': form})

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_manager'] = self.request.user.groups.filter(name='Manager').exists()
        context['is_operator'] = self.request.user.groups.filter(name='Operator').exists()
        return context

# Inventory
class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'inventories'
    permission_classes = [IsAuthenticated, IsManager]

class AddInventoryItem(LoginRequiredMixin, CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('inventory-list')
    permission_classes = [IsAuthenticated, IsManager]

    def form_valid(self, form):
        return super().form_valid(form)
    
class EditInventoryItem(LoginRequiredMixin, UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('inventory-list')
    permission_classes = [IsAuthenticated, IsManager]

class DeleteInventoryItem(LoginRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'delete_item.html'
    success_url = reverse_lazy('inventory-list')
    context_object_name = 'item'
    permission_classes = [IsAuthenticated, IsManager]

# Inbound
class InboundListView(LoginRequiredMixin, ListView):
    model = Inbound
    template_name = 'inbound_list.html'
    context_object_name = 'inbounds'
    permission_classes = [IsAuthenticated]

class AddInboundItem(LoginRequiredMixin, CreateView):
    model = Inbound
    form_class = InboundForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('inbound-list')
    permission_classes = [IsAuthenticated]

    def form_valid(self, form):
        return super().form_valid(form)
    
class EditInboundItem(LoginRequiredMixin, UpdateView):
    model = Inbound
    form_class = InboundForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('inbound-list')
    permission_classes = [IsAuthenticated]

class DeleteInboundItem(LoginRequiredMixin, DeleteView):
    model = Inbound
    template_name = 'delete_item.html'
    success_url = reverse_lazy('inbound-list')
    context_object_name = 'item'
    permission_classes = [IsAuthenticated]

# Outbound
class OutboundListView(LoginRequiredMixin, ListView):
    model = Outbound
    template_name = 'outbound_list.html'
    context_object_name = 'outbounds'
    permission_classes = [IsAuthenticated]

class AddOutboundItem(LoginRequiredMixin, CreateView):
    model = Outbound
    form_class = OutboundForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('outbound-list')
    permission_classes = [IsAuthenticated]

    def form_valid(self, form):
        return super().form_valid(form)
    
class EditOutboundItem(LoginRequiredMixin, UpdateView):
    model = Outbound
    form_class = OutboundForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('outbound-list')
    permission_classes = [IsAuthenticated]

class DeleteOutboundItem(LoginRequiredMixin, DeleteView):
    model = Outbound
    template_name = 'delete_item.html'
    success_url = reverse_lazy('outbound-list')
    context_object_name = 'item'
    permission_classes = [IsAuthenticated]

# DRF
class EditOutboundItem(LoginRequiredMixin, UpdateView):
    model = Outbound
    form_class = OutboundForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('outbound-list')

class DeleteOutboundItem(LoginRequiredMixin, DeleteView):
    model = Outbound
    template_name = 'delete_item.html'
    success_url = reverse_lazy('outbound-list')
    context_object_name = 'item'

class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated, IsManager]

class InventoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated, IsManager]

class InboundListCreateView(generics.ListCreateAPIView):
    queryset = Inbound.objects.all()
    serializer_class = InboundSerializer
    permission_classes = [IsAuthenticated]

class InboundRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inbound.objects.all()
    serializer_class = InboundSerializer
    permission_classes = [IsAuthenticated]

class OutboundListCreateView(generics.ListCreateAPIView):
    queryset = Outbound.objects.all()
    serializer_class = OutboundSerializer
    permission_classes = [IsAuthenticated]

class OutboundRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outbound.objects.all()
    serializer_class = OutboundSerializer
    permission_classes = [IsAuthenticated]