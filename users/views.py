from django.shortcuts import render
from django.http import JsonResponse

def test(request):
    print('test ')
    data = {"msg": "travistest"}
    return JsonResponse(data, safe=False)