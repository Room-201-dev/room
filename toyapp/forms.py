from django import forms
from .models import WorkSpaceModel


class WorkSpaceForm(forms.Form):
    prototype_form = forms.ModelChoiceField(
        label='Select',
        queryset=WorkSpaceModel.objects.all(),
        to_field_name='prototype',
        required=True,
        empty_label=None,
    )


class RadioForm(forms.Form):
    day = forms.MultipleChoiceField(
        choices=(
            ('日', '日'),
            ('月', '月'),
            ('火', '火'),
            ('水', '水'),
            ('木', '木'),
            ('金', '金'),
            ('土', '土'),
        ),
        label='曜日',
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'column'
        })
    )
