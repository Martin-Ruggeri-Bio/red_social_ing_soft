from rest_framework import serializers
from users.models import User


# un serializador nos permite convertir objetos de python en json
# es similar a un formulario donde lo defines y tienes los distintos campos
class UserSerializer(serializers.ModelSerializer):
    '''Serializa objeto de perfil de un usuario'''
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        '''Creaturn y retornar nuevo usuario'''
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user
    
    def update(self, instance, validated_data):
        '''Creaturn y retornar nuevo usuario'''
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
