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






































#def  databaseEmDjango():
    
#    data = User.objects.get(pk='thiago_nick')   #OBJETO

 #   data = User.objects.filter(user_age = '25')  #QUERYSET

  #  data = User.objects.exclude(user_age = '25')  #QUERYSET(NÃO RETORNA OBJ - FAZER FOR E JOGAR EM LISTA) DIFERENTE DE FILTER ( MOSTRA O QUE NÃO É TAL VALOR)
    
   # data.save()

    #data.delete()