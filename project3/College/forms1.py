from django import forms
from College.models import Coll

class CollForm(forms.ModelForm):
    class Meta:
        model = Coll
        fields = '__all__'