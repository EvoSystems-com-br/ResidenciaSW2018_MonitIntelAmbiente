from rest_framework import serializers
from .models import User, Camera


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User(
            name=validated_data.get('name', None),
            email=validated_data.get('email', None),
            address=validated_data.get('address', ""),
            cpf=validated_data.get('cpf', None),
        )
        user.set_password(validated_data.get('password', None))
        user.save()
        return user

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('url', 'id', 'email', 'password',
                  'name', 'cpf', 'address')
        extra_kwargs = {
            'url': {
                'view_name': 'users:user-detail',
            }
        }


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'
