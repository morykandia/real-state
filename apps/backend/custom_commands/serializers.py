from rest_framework import serializers
from custom_commands.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email','password')

    def validate(self, data):
        user = User(**data)
        password = data.get('password')

        try:
          validate_password(password, user)
        except exceptions.ValidationError as e:
          serializer_errors = serializers.as_serializer_error(e)
          raise exceptions.ValidationError(
            {'password': serializer_errors['non_field_errors']}
          )

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
          first_name=validated_data['first_name'],
          last_name=validated_data['last_name'],
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password'],
        )

        return user

class UserAcountSerializer(serializers.ModelSerializer):  
    class Meta:
        model = UserAccount
        fields = ['id','first_name', 'last_name','email', 'username', 'is_staff']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

    def validate_name (self,value):
        if Category.objects.filter(name=value).exists():
             raise serializers.ValidationError('Category already exists')
        return value


class BlogPostSerializer(serializers.ModelSerializer):
    #author = UserAcountSerializer()
    category = CategorySerializer(many=True)   
    class Meta:    
        model = BlogPost
        fields = ['id','title','published', 'date', 'category']
    
    def validate_name(self, value):
        if BlogPost.objects.filter(title=value).exist():
            raise serializers.ValidationError('Blog already exists')
        return value