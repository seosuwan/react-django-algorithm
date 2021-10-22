from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.common.models import ValueObject, Reader, Printer
import matplotlib.pyplot as plt

from admin.aiTrader.models import AiTrader


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    AiTrader().process()
    return JsonResponse({'AiTrader': 'Crawling Success'})

