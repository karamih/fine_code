from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'password']

    def validate_username(self, value):
        if UserModel.objects.filter(username=value).exists():
            raise serializers.ValidationError({'details': 'This username is already registered.'})
        return value

    def create(self, validated_data):
        try:
            password = validated_data.pop('password')
            user = UserModel.objects.create_user(
                username=validated_data['username'],
                password=password
            )
            return user
        except Exception as e:
            raise serializers.ValidationError({'details': str(e)})
