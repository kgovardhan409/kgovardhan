from django import forms

class Subscribe(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(max_length=300)

    def __str__(self):
        return self.name