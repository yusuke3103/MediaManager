from django import forms


class SyoboCalTitleSearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)
    
class TitleRegistForm(forms.Form):
    pulldown = forms.ChoiceField(widget=forms.RadioSelect, choices=[(0,'----'),(0,'----'),(0,'----')])