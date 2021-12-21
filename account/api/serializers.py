from rest_framework import serializers

from account.models import CustomUser


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70, label='username')
    password = serializers.CharField(min_length=6, max_length=100, label='password')
    confirm_password = serializers.CharField(min_length=6, max_length=100, label='confirm_password', write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(username=validated_data['username'],)
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError(_('this username already exist'))
        elif password != confirm_password:
            raise serializers.ValidationError(_('The two password fields didn’t match'))
        return attrs
