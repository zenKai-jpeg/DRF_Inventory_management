from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Inventory, Inbound, Outbound

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = '__all__'

class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = '__all__'