from django import forms
from .models import Book
from .models import Login

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','producedby','purchaseDate','isAvailable']
        widgets = {
            'purchaseDate': forms.SelectDateWidget
        }
        #'purchaseDate'

class newLoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['Loginid','password','mail']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['Loginid','password']