from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.http import Http404
from custom_commands.permissions import  IsAdminAuthenticated
from custom_commands.models import *
from custom_commands.serializers import *


class RegisterView(APIView):
    def post(self, request):
      data = request.data

      serializer = UserCreateSerializer(data=data)

      if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      user = serializer.create(serializer.validated_data)
      user =UserAcountSerializer(user)
      return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user = UserAcountSerializer(user)
        return Response(user.data, status=status.HTTP_200_OK)
    

class UserAccountAPIView(APIView):
    #permission_classes = [IsAdminAuthenticated]
    def get(self, *args, **kwargs):
        allUsers = UserAccount.objects.all()
        serializer = UserAcountSerializer(allUsers, many=True)
        return Response(serializer.data)

class UserAcccountAPIViewUpdateOrDelete(APIView):
    #permission_classes = [IsAdminAuthenticated]
    def get_object(self, pk):
        try:
            return UserAccount.objects.get(pk=pk)
        except UserAccount.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserAcountSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserAcountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#all can see categories 
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
#only admin can post the category(security acces)
class CategoryAPICreate(APIView):
    #permission_classes = [permissions.IsAdminUser]  
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#all can see  this category  specific (security acces )
class CategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
#only admin can deleted or update 
class CategoryUpdateOrDeletedAPIView(APIView):
    #permission_classes = [permissions.IsAdminUser]
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class BlogPostAPIView(APIView):
    #permission_classes = [permissions.IsAdminUser]
    def get(self, *args, **kwargs):
        articles = BlogPost.objects.all()
        serializer = BlogPostSerializer(articles, many=True)
        return Response(serializer.data)

class BlogPostPublishedTrue(APIView):
    def get(self,  *args, **kwargs):
        articles = BlogPost.objects.all().filter(published=True)
        serializer = BlogPostSerializer(articles, many=True)
        return Response(serializer.data)

class BlogPostCreateAPIView(APIView):
    #permission_classes = [permissions.IsAdminUser]
    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class BlogPostDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = BlogPostSerializer(article)
        return Response(serializer.data)


class BlogPostUpdateOrDeleted(APIView): 
    #permission_classes = [permissions.IsAdminUser]
    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404


    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = BlogPostSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

