from django.forms import ModelForm , TextInput
from .models import CityData
class CityForm(ModelForm):
    class Meta:
        model = CityData
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class':'input','placeholder':'City Name'})}
