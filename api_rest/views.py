from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.


@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = User.objects.all()       #obs: Returns queryset

        serialiezer = UserSerializer(users, many = True) # Serialiezer the object data into json, parameter 'many' because are queryset

        return Response(serialiezer.data) # return serielizer
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_nick(request,nick):

    try:
      user = User.objects.get(pk=nick)

    except :
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serialiezer = UserSerializer(user)
        return Response(serialiezer.data)


@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):
    if request.method == 'GET':
      
      try:
            user = request.GET.get('user')   
            user_nick = User.objects.get(pk=user)
            serializer = UserSerializer(user_nick)
            return Response(serializer.data,status=status.HTTP_200_OK)
      except User.DoesNotExist:  # Caso o usuário não seja encontrado
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
          
      except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
      
    if request.method == 'POST':
       try:
          new_user = request.data
          serializer = UserSerializer(data = new_user)
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
       except:
          return Response(status=status.HTTP_400_BAD_REQUEST)

    
            
        
       































#def  databaseEmDjango():
    
#    data = User.objects.get(pk='thiago_nick')   #OBJETO

 #   data = User.objects.filter(user_age = '25')  #QUERYSET

  #  data = User.objects.exclude(user_age = '25')  #QUERYSET(NÃO RETORNA OBJ - FAZER FOR E JOGAR EM LISTA) DIFERENTE DE FILTER ( MOSTRA O QUE NÃO É TAL VALOR)
    
   # data.save()

    #data.delete()