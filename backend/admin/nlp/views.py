from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.nlp.models import Imdb, NaverMovie


@api_view(['GET'])
@parser_classes([JSONParser])
def Imdb_process(request):
    Imdb().Imdb_process()
    return JsonResponse({'Imdb_process': 'Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMovie().naver_process()
    return JsonResponse({'Imdb_process': 'Success'})