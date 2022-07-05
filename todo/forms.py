from django import forms





class TodoListForm (forms.Form):
    task = forms.CharField(max_length= 500, help_text='')
    
    class Meta:
        help_texts = {
            "task":None,
        }