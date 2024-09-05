from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    InventoryListCreateView,
    InventoryRetrieveUpdateDestroyView,
    InboundListCreateView,
    InboundRetrieveUpdateDestroyView,
    OutboundListCreateView,
    OutboundRetrieveUpdateDestroyView,
    SignUpView,
    InventoryListView, 
    AddInventoryItem, 
    EditInventoryItem, 
    DeleteInventoryItem,
    InboundListView, 
    AddInboundItem, 
    EditInboundItem, 
    DeleteInboundItem,
    OutboundListView, 
    AddOutboundItem, 
    EditOutboundItem, 
    DeleteOutboundItem
)

urlpatterns = [
    # api
    path('inventory_api/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory_api//<int:pk>/', InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),
    path('inbound_api/', InboundListCreateView.as_view(), name='inbound-list-create'),
    path('inbound_api/<int:pk>/', InboundRetrieveUpdateDestroyView.as_view(), name='inbound-detail'),
    path('outbound_api/', OutboundListCreateView.as_view(), name='outbound-list-create'),
    path('outbound_api/<int:pk>/', OutboundRetrieveUpdateDestroyView.as_view(), name='outbound-detail'),

    # Inventory
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/add/', AddInventoryItem.as_view(), name='inventory-add'),
    path('inventory/edit/<int:pk>/', EditInventoryItem.as_view(), name='inventory-edit'),
    path('inventory/delete/<int:pk>/', DeleteInventoryItem.as_view(), name='inventory-delete'),

    # Inbound
    path('inbound/', InboundListView.as_view(), name='inbound-list'),
    path('inbound/add/', AddInboundItem.as_view(), name='inbound-add'),
    path('inbound/edit/<int:pk>/', EditInboundItem.as_view(), name='inbound-edit'),
    path('inbound/delete/<int:pk>/', DeleteInboundItem.as_view(), name='inbound-delete'),

    # Outbound
    path('outbound/', OutboundListView.as_view(), name='outbound-list'),
    path('outbound/add/', AddOutboundItem.as_view(), name='outbound-add'),
    path('outbound/edit/<int:pk>/', EditOutboundItem.as_view(), name='outbound-edit'),
    path('outbound/delete/<int:pk>/', DeleteOutboundItem.as_view(), name='outbound-delete'),

    # User
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]