from django import forms
from .models import Row

class RowFill(forms.ModelForm):
    class Meta:
        model = Row
        fields = ('dataset','point','client_id','client_name')
    