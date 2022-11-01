from django.forms import ModelForm
from faperta.models import Dosen

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'
