from django import forms
#
from .models import User
#
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):

    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña'
            }
        )
    )

    confirm_password = forms.CharField(
        required=True,
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirmar Contraseña'
            }
        )
    )


    class Meta:
        model = User
        fields = (
            'full_name',
            'email',
            'address',
            'date_birth',
            'phone',
            'photo',
        )

        widgets = {
            'full_name' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingresa nombre completo'
                }
            ),

            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'myemail@email.com'
                }
            ),

            'address' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingresa Direccion'
                }
            ),

            'date_birth' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            ),

            'phone' : forms.TextInput(
                attrs={
                    'placeholder' : 'Telefono contacto'
                }
            ),
        }
    

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este usuario ya existe')
        
        return email
    

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']

        if confirm_password != self.cleaned_data['password']:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return confirm_password


class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder' : 'Email de usuario'
            }
        )
    )


    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'label':'Contraseña de usuario'
            }
        )
    )


    def clean_password(self):
        #cleaned_data = super(LoginForm,self).clean()
        
        correo = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = authenticate(email=correo, password=password)

        if not user:
            raise forms.ValidationError('Usuario o contraseña incorrectos')

        #return cleaned_data
        return password