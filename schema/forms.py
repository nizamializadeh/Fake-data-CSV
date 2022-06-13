from django import forms
from .models import Column


class ColumnForm(forms.ModelForm):

    class Meta:
        model = Column
        fields = '__all__'
