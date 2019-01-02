from django import forms

from animes.models import Title, SubTitle


class TitleListForm(forms.Form):
    class Meta:
        model = Title
        fields = ('tid','title','firstYear','firstMonth','firstEndYear','firstEndMonth','comment')
    
class SyoboCalTitleSearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)
    
class TitleResultForm(forms.Form):
    pulldown = forms.ChoiceField(widget=forms.RadioSelect, choices=[])
    
    class Meta:
        model = Title
        fields = ('tid','title','firstYear','firstMonth','firstEndYear','firstEndMonth','comment')

class DetailForm(forms.Form):
    class Meta:
        model = SubTitle
        fields = {'rno','subtitle'}