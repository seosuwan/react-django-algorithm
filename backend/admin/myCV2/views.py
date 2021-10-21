from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myCV2.models import MyCV2


@api_view(['GET'])
@parser_classes([JSONParser])
def lena(request):
    MyCV2().lena()
    return JsonResponse({'Cv2': 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def girl(request):
    MyCV2().girl()
    return JsonResponse({'Cv2': 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def face_detect(request):
    MyCV2().face_detect()
    return JsonResponse({'Cv2': 'Success'})