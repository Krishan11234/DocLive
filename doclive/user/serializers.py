from rest_framework import serializers
from user.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    # fields = ["id", "first_name", "last_name", "username", "email", "phone_number", "password", "re_password"]
    fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
  username = serializers.CharField(required=True,
  validators=[UniqueValidator(queryset=CustomUser.objects.all())]
  )
  email = serializers.EmailField(required=True,
    validators=[UniqueValidator(queryset=CustomUser.objects.all())]
  )
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  re_password = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = CustomUser
    fields = ["id", "first_name", "last_name", "username", "email", "phone_number", "password", "re_password"]
    extra_kwargs = {'first_name': {'required': True},'last_name': {'required': True},'username': {'required': True},'email': {'required': True},
      'phone_number': {'required': True},'password': {'required': True},'re_password': {'required': True}
    }

  def validate(self, attrs):
    if attrs['password'] != attrs['re_password']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})
    return attrs


  def create(self, validated_data):
    user = CustomUser.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      phone_number=validated_data['phone_number'],
      re_password=validated_data['re_password']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user