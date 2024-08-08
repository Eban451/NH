from django import forms
from .models import Usuario, Propiedad, Direccion

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'departamento', 'comuna']

class UsuarioRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombres', 'rut', 'telefono', 'tipo_usuario', 'correo']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales', 
            'estacionamientos', 'habitaciones', 'banos', 
            'precio_arriendo', 'garantia', 'tipo_propiedad', 
            'disponible'
        ]
