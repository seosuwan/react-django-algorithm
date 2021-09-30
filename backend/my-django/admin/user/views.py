from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.user.models import UserVo
from admin.user.serializer import UserSerializers


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        all_users = UserVo.objects.all()
        serializer = UserSerializers(all_users, many=True)
        return JsonResponse(data=serializer, safe=False)
    elif request.method == 'POST':
        new_user = request.data['body']
        print(new_user)
        serializer = UserSerializers(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': 'f{welcome, {ser}}'}, staus=201)
        return JsonResponse(serializer.errors, staus=status.HTTP_400_BAD_REQUEST)
# Create your views here.
