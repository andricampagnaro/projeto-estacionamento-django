from django import forms

from .models import Vaga

class MenuForm(forms.ModelForm):

    class Meta:
        model = Vaga
        fields = ('nome_vaga', 'status_vaga',)