from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from django import forms

from ..models import myUser

class RegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    
    class Meta:
        model = myUser
        fields = ["userName", "name", "callNumber", "address", "is_seller"]
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #return HttpResponse("Valid")
            form.save()
            return redirect("shopapp:index")
        else :
            return HttpResponse("Invalid (Maybe password didn't match or too short/simple)")
    else: form = RegisterForm()
    return render(request, 'register.html', {"form" : form})