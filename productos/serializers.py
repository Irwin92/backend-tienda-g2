from rest_framework import serializers
from .models import Producto, Categoria

# modelo = Producto  Indica que modelo se transformara y validara
# fields= '__all__'  Expone todos los campos del modelo
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields= '__all__'

    def validate_precio(self,value):
        if value <=0:
            raise serializers.ValidationError(
                'El precio debe ser mayor que cero'
                )
        return value
    
    def validate_stock(self,value):
            if value <0:
                raise serializers.ValidationError(
                    'El stock no puede ser negativo.'
                    )
            return value
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields= '__all__'

    def validate_nombre(self,value):

        nombre_limpio= value.strip()
        
        if len(nombre_limpio) < 3:
            raise serializers.ValidationError(
                'El nombre debe tener al menos 3 caracteres.'
                )
        return nombre_limpio
   



