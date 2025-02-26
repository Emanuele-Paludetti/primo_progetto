import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Evento

def Index_evento(request):
    return render(request, "Index_evento.html")

def query_a(request):
    query_a = Evento.objects.order_by('-Data inizio').first()
     

    context = {
        'query_a': query_a,
    }

    return render(request,'view_a.html',context)


def query_b(request):
    query_b = Evento.objects.all()

    context = {
        'query_b': query_b,
    }
    
    
    return render(request,'view_b.html',context)

def query_c(request):
    query_c = Evento.objects.filter(data_inizio__gt=datetime.date(2025,6,1))

    context = {
        'query_c': query_c,
    }
    
    
    return render(request,'view_c.html',context)

def query_d(request):
    query_d = Evento.objects.filter(posti_disponibili__gte=80)

    context = {
        'query_d': query_d,
    }
    
    
    return render(request,'view_d.html',context)

def query_e(request):
    query_e = Evento.objects.filter(data_fine__lt=datetime.date(2025,5,31))

    context = {
        'query_e': query_e,
    }
    
    
    return render(request,'view_e.html',context)

def query_f(request):
    query_max = Evento.objects.order_by('-posti_disponibili').first()
    query_min = Evento.objects.order_by('posti_disponibili').first()
    
    totale_posti=0
    query_tot = Evento.objects.all()
    for evento in query_tot:
        totale_posti += evento.posti_disponibili


    context = {
        'query_max': query_max,
        'query_min': query_min,
        'query_tot': totale_posti
    }
    
    
    return render(request,'view_f.html',context)