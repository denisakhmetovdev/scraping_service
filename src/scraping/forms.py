from django import forms

from .models import City, Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  to_field_name='slug', required=False, empty_label='Выберите город',
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Город'
                                  )
    language = forms.ModelChoiceField(queryset=Language.objects.all(),
                                      to_field_name='slug', required=False, empty_label='Выберите ЯП',
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Специальность'
                                      )
