from django import forms

class CreateTodo(forms.Form):
    item = forms.CharField(label="Enter the item", max_length=300)
