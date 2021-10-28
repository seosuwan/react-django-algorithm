from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.contrib.auth import login as auth_login

from admin.user.models import User
from admin.user.serializer import UserSerializer


@api_view(['GET', 'POST','PUT'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        all_users = User.objects.all()
        ic(all_users)
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer, safe=False)
    elif request.method == 'POST':
        new_user = request.data
        ic(new_user)
        # print(new_user)
        serializer = UserSerializer(data=new_user)
        ic(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
       return None

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    # 로그인이 되어있다면 아래 함수를 수행하기에 적합하지 않으므로 바로 redirect 한다.
    if request.user.is_authenticated:
        return JsonResponse('articles:index')

    if request.method == 'POST':
        # 첫번째 인자로 request 를 받아야 한다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효성 검사를 통과하면 세션을 create 해야 함 -> login()
            auth_login(request, form.get_user())
            # url 에 next 가 있을 때랑 없을때 결과가 다름
            return JsonResponse(request.GET.get('next') or 'articles:index')
    else:
        # 로그인에 필요한 빈 종이를 생성해서 lognin.html 에 전달
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return JsonResponse(request, 'accounts/login.html', context)


@api_view(['GET','POST'])
@parser_classes([JSONParser])
def users(request): #오버로딩
    pass