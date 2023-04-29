from rest_framework import serializers
from user.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

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
    fields = ["id", "gender", "first_name", "last_name", "username", "email", "phone_number", "password", "re_password"]
    extra_kwargs = {'gender': {'required': True},'first_name': {'required': True},'last_name': {'required': True},'username': {'required': True},'email': {'required': True},
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
      gender=validated_data['gender'],
      phone_number=validated_data['phone_number'],
      re_password=validated_data['re_password']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(
      label="Username",
      write_only=True
    )
    password = serializers.CharField(
      label="Password",
      # This will be used when the DRF browsable API is enabled
      style={'input_type': 'password'},
      trim_whitespace=False,
      write_only=True
    )

    def validate(self, attrs):
      username = attrs.get('username')
      password = attrs.get('password')

      if username and password:
        # Try to authenticate the user using Django auth framework.
        user = authenticate(request=self.context.get('request'),
                            username=username, password=password)
        if not user:
          msg = 'Access denied: wrong username or password.'
          raise serializers.ValidationError(msg, code='authorization')
      else:
        msg = 'Both "username" and "password" are required.'
        raise serializers.ValidationError(msg, code='authorization')
      attrs['user'] = user
      return attrs