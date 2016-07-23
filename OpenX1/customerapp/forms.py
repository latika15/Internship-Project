from django import forms
from components.models import CustomerIssue, Suggestion, Category


class ReportIssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReportIssueForm, self).__init__(*args, **kwargs)
        self.fields['issue_img'].required = False
    class Meta:
        model = CustomerIssue  
        fields = ['issue_title','issue_subcategory','issue_description', 'issue_img']
        
class SuggestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SuggestionForm, self).__init__(*args, **kwargs)
        self.fields['suggestion_title'].required = True
        self.fields['suggestion_description'].help_text = ''
        self.fields['suggestion_category'] = forms.ChoiceField(choices=[(category.category_name, category)
            for category in Category.objects.all()])
    class Meta:
        model = Suggestion
        fields = ['suggestion_title','suggestion_description']

    suggestion_category = forms.ChoiceField()
        
  

        