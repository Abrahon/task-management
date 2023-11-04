from django import forms
from task.models import TaskStoreModel

class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskStoreModel
        fields = ['id','title','description','status','priority','due_date','image']
        
