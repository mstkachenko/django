from django import forms
from products.models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-field'}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': 'form-field'}
        )
    )


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={'class': 'form-field'}
            ),
            'description': forms.widgets.Textarea(
                attrs={'class': 'form-field'}
            ),
        }
