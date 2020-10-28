from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Plan

def holaMundoDesdePlanes(request):
    return HttpResponse('Hola desde Planes')

def detallePlan(request, plan_id):
    try:
        plan = Plan.objects.get(pk=plan_id)
    except Plan.DoesNotExist:
        return JsonResponse({'error': 'El plan no existe'})

    return JsonResponse({'data': plan})
