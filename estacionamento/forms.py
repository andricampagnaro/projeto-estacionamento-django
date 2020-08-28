from django import forms

from .models import Vaga

class MenuForm(forms.ModelForm):

    class Meta:
        model = Vaga
        fields = ('status_vaga',)