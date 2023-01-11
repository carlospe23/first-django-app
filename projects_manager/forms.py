from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label = "Task Title", max_length = 200)
    description = forms.CharField(widget = forms.Textarea, label = "Task Description")

class CreateNewProject(forms.Form):
    title = forms.CharField(label = "Project Title", max_length = 200)