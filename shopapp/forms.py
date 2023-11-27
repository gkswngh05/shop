from django import forms

from .models import myUser, Order

from django.contrib.auth.forms import ReadOnlyPasswordHashField

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
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = myUser
        fields = ['userName', 'name', 'callNumber', 'address', "is_active", "is_seller", "is_admin"]
        
        
class OrderForm(forms.ModelForm):
    
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request")
    #     super(OrderForm, self).__init__(*args, **kwargs)
       
    def save(self, commit=True):
        order = super().save(commit=False)
        # order.set_customer(self.request.user)
        if commit == True:
            order.save()
        return order
        

    class Meta:
        model = Order
        fields = ["receiverName", "receiverNumber", "receiverAddress",
                  "customer", "itemCode", "amount"]