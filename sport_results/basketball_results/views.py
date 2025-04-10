from django.shortcuts import render
from .models import BasketballMatch


def match_list(request):
    matches = BasketballMatch.objects.all().order_by('-date')
    return render(request, 'match_list.html', {'matches': matches})




