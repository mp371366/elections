from django.shortcuts import render
from .models import *

def main(request):
    context = {
        'title': 'Wyniki wyborów w kraju',
        'current_name': 'Polska',
        'map_data': [ { 'name': str(v), 'value': 50 } for v in Voivodeship.objects.all() ],
        'results': [ { 'name': str(c), 'value': 50 } for c in Candidate.objects.all() ],
        'links': [ { 'name': str(v), 'link': v.name } for v in Voivodeship.objects.all() ],
    }

    return render(request, 'links.html', context)

def voivodeship(request, name):
    v = Voivodeship.objects.get(name=name)
    n = str(v).lower()

    context = {
        'title': 'Wyniki wyborów - {0}'.format(n),
        'current_name': '{0}'.format(str(v)),
        'results': [ { 'name': str(c), 'value': 50 } for c in Candidate.objects.all() ],
        'links': [ { 'name': str(d), 'link': d.name } for d in District.objects.filter(voivodeship__name=name) ],
    }
    
    return render(request, 'links.html', context)

def district(request, name):
    d = Dsitrict.objects.get(name=name)
    n = str(d).lower()

    context = {
        'title': 'Wyniki wyborów - {0}'.format(n),
        'current_name': '{0}'.format(str(d)),
        'results': [ { 'name': str(c), 'value': 50 } for c in Candidate.objects.all() ],
        'links': [ { 'name': str(u), 'link': u.name } for d in Unit.objects.filter(district__name=name) ],
    }
    
    return render(request, 'links.html', context)

def unit(request, name):
    u = Unit.objects.get(name=name)
    n = str(u).lower()

    context = {
        'title': 'Wyniki wyborów - {0}'.format(n),
        'current_name': '{0}'.format(str(u)),
        'results': [ { 'name': str(c), 'value': 50 } for c in Candidate.objects.all() ],
    }
    
    return render(request, 'basic.html', context)
