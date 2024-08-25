from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'tipo']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 100:
            raise forms.ValidationError("El precio no puede ser menor a 100 pesos.")
        return precio
