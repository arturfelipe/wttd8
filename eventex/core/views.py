# coding: utf-8

from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Bem-vindo ao eventEX!')
