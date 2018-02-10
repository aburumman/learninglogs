from django import forms
from .models import Topic, Entry

# Model Form is used to creat form from the models field
class TopicForm(forms.ModelForm):
    ''' Create a form for the topic '''
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    ''' create a form for the entry '''
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
