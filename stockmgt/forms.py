from django import forms
from django.utils import timezone

from .models import Stock, StockHistory


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        # for instance in Stock.objects.all():
        #     if instance.category == category:
        #         raise forms.ValidationError(f'{category} is already created')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        for instance in Stock.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError(str(item_name) + ' is already created')
        return item_name


class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)


    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'export_to_CSV']


class StockHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                     required=False, initial=timezone.now)
    end_date = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                   required=False, initial=timezone.now)


    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'export_to_CSV', 'start_date', 'end_date']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = StockHistory
        fields = ['category', 'item_name', 'quantity']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity', 'receive_by']


class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']
