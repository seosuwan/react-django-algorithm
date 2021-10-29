from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.user import serializer
from admin.user.models import User
from admin.user.serializer import UserSerializer
from icecream import ic


@api_view(['GET'])
def detail(request, username):
    # ic(username)
    dbUser = request.data
    # ic(dbUser)
    # ic(type(dbUser))
    #ic| type(dbUser): <class 'dict'>
    detailUser = User.objects.get(pk=username)
    # ic(detailUser)
    # ic(type(detailUser))
    userSerializer = UserSerializer(detailUser, many=False)
    return JsonResponse(data=userSerializer.data, safe=False)


@api_view(['GET', 'POST', 'PUT'])
@parser_classes([JSONParser])
def users(request):
    print('들어옴=========================================')
    if request.method == 'GET':
        all_users = User.objects.all()
        ic(all_users)
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer, safe=False)
    elif request.method == 'POST':
        new_user = request.data
        ic(new_user)
        print(new_user)
        serializer = UserSerializer(data=new_user)
        ic(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
       return None


@api_view(['POST'])
def login(request):
    try:
        print('들어왔다고 해줘........여기까지만이라도.........................')
        loginUser = request.data
        ic(loginUser)
        print(f'============={type(loginUser)}')
        dbUser = User.objects.get(pk =loginUser['username'])
        if loginUser['password'] == dbUser.password:
            print('======================로그인 성공')
            userSerializer = UserSerializer(dbUser, many=False)
            ic(UserSerializer)
            return JsonResponse(data=userSerializer.data, safe=False)
        else:
            print('===========================비밀번호 오류')
            return JsonResponse(data={'rsult' :'PASSWORD-FAIL' }, status= 201)

        return JsonResponse(data=serializer, safe=False)
    except User.DoesNotExist:
        print('*', *100)
        print('에러에러에러에러에러 발생!!!!!!!!!!!!!!!!!!!!!')
        return JsonResponse(data={'result':'USERNAME-FAIL'}, status=201)

@api_view(['DELETE'])
def remove(request, id): #오버로딩
    pass


@api_view(['GET'])
@parser_classes([JSONParser])
def list(request): #오버로딩
    lists = request.data
    # ic(lists)
    if request.method == 'GET':
        all_users = User.objects.all()
        ic(all_users)
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer, safe=False)
    # lists = User.objects.all()
    # ic(lists)
    # userSerializer = UserSerializer(lists, many=True)
    # ic(userSerializer)
    # return JsonResponse(data=userSerializer, safe=False)
