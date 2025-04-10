from django.shortcuts import render
from .models import BasketballMatch
from django.db.models import Q


def match_list(request):
    matches = BasketballMatch.objects.all().order_by('-date')

    query_team = request.GET.get('team')
    query_date = request.GET.get('date')

    if query_team:
        matches = matches.filter(
            Q(team1__icontains=query_team) | Q(team2__icontains=query_team))

    if query_date:
        matches = matches.filter(date=query_date)

    return render(request, 'match_list.html', {'matches': matches, 'query_team': query_team or '', 'query_date': query_date or ''})










