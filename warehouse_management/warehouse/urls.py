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
    path('api/inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('api/inventory/<int:pk>/', InventoryRetrieveUpdateDestroyView.as_view(), name='inventory-detail'),
    path('api/inbound/', InboundListCreateView.as_view(), name='inbound-list-create'),
    path('api/inbound/<int:pk>/', InboundRetrieveUpdateDestroyView.as_view(), name='inbound-detail'),
    path('api/outbound/', OutboundListCreateView.as_view(), name='outbound-list-create'),
    path('api/outbound/<int:pk>/', OutboundRetrieveUpdateDestroyView.as_view(), name='outbound-detail'),

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