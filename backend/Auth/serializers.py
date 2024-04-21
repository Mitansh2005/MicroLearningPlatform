from .models import CustomUser
from rest_framework import serializers
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from .utils import Util

class UserRegisterationSerializer(serializers.ModelSerializer):
  password2=serializers.CharField(style={'input_type':'password'},write_only=True)
  class Meta:
    model=CustomUser
    fields=['email','username','password','password2']
    extra_kwargs={
      'password':{'write_only':True}
    }
  def validate(self, data):
    password=data.get('password')
    password2=data.get('password2')
    if password !=password2:
      raise serializers.ValidationError('Password and Confirm Password does not match')

    return data
  
  def create(self, validated_data):
   return CustomUser.objects.create_user(**validated_data)

class CustomUserLoginSerializer(serializers.ModelSerializer):
  email=serializers.EmailField(max_length=255)
  class Meta:
    model=CustomUser
    fields=['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model=CustomUser
    fields=['id','email','username']

class UserChangePasswordSerializer(serializers.Serializer):
  password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
  password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
  class Meta:
    fields=['password','password2']
  def validate(self,data):
    user=self.context.get('user')
    password=data.get('password')
    password2=data.get('password2')
    if password !=password2:
     raise serializers.ValidationError('Password and Confirm Password does not match')
    user.set_password(password)
    user.save()
    return data
  
