from django import forms
from components.models import BroadcastMessage, SubCategory, GovTable, Category


class AddOfficialForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(AddOfficialForm, self).__init__(*args, **kwargs)
        depthead = GovTable.objects.get(username = user)
        self.fields['official_subcategory'] = forms.ChoiceField(choices=[(subcategory.subcategory_name, subcategory)
            for subcategory in SubCategory.objects.filter(category = depthead.category)])
    
    email = forms.EmailField(required = True)
    official_subcategory = forms.ChoiceField()
    
class AddDeptHeadForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddDeptHeadForm, self).__init__(*args, **kwargs)
        self.fields['depthead_category'] = forms.ChoiceField(choices=[(category.category_name, category)
            for category in Category.objects.all()])
    
    email = forms.EmailField(required = True)
    depthead_category = forms.ChoiceField()    

class BroadcastForm(forms.ModelForm):
    class Meta:
        model = BroadcastMessage 
        fields = ['broadcast_msg']