from django import forms

class createNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", 
        max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion de la tarea",
        widget=forms.Textarea(attrs={'class' : 'input'}))

class createNewProject(forms.Form):
    name = forms.CharField(label="nombre del proyecto", max_length=200, 
                           widget=forms.TextInput(attrs={'class' : 'input'}))