
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count, Avg, Max, F
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import BasketballMatchForm
from .models import BasketballMatch


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


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Užsiregistravote sėkmingai, galite prisijungti.')
        return response


class CustomLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request ,'Sėkmingai prisijungėte')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Sėkmingai atsijungėte')
        return super().dispatch(request, *args, **kwargs)


class MatchCreateView(LoginRequiredMixin ,CreateView):
    model = BasketballMatch
    form_class = BasketballMatchForm
    template_name = 'add_match.html'
    success_url = reverse_lazy('match_list')

    def form_valid(self, form):
        messages.success(self.request, 'Rungtynės pridėtos sėkmingai')
        return super().form_valid(form)


class MatchUpdateView(LoginRequiredMixin, UpdateView):
    model = BasketballMatch
    form_class = BasketballMatchForm
    template_name = 'edit_match.html'
    success_url = reverse_lazy('match_list')

    def form_valid(self, form):
        messages.success(self.request, 'Rungtynės sėkmingai atnaujintos')
        return super().form_valid(form)

class MatchDeleteView(LoginRequiredMixin, DeleteView):
    model = BasketballMatch
    template_name = 'delete_match.html'
    success_url = reverse_lazy('match_list')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'Rungtynės ištrintos sėkmingai')
        return super().delete(request, *args, **kwargs)


# statistics

def statistics_view(request):
    matches = BasketballMatch.objects.all()

    team_games = {}
    for match in matches:
        team_games[match.team1] = team_games.get(match.team1, 0) + 1
        team_games[match.team2] = team_games.get(match.team2, 0) + 1

    team_wins = {}
    for match in matches:
        if match.score1 > match.score2:
            winner = match.team1
        elif match.score1 < match.score2:
            winner = match.team2
        else:
            continue
        team_wins[winner] = team_wins.get(winner, 0) + 1

    from collections import defaultdict
    team_score = defaultdict(list)

    for match in matches:
        team_score[match.team1].append(match.score1)
        team_score[match.team2].append(match.score2)

    team_avg_score = {team: round(sum(scores) / len(scores), 2) for team, scores in team_score.items() }

    top_score = matches.order_by('-score1', '-score2').first()
    top_team = None
    top_points = 0
    if top_score:
        top_team = top_score.team1 if top_score.score1 > top_score.score2 else top_score.team2
        top_points = top_score.score1 if top_score.score1 > top_score.score2 else top_score.score2

    team_games_sorted = dict(sorted(team_games.items(), key=lambda item: item[1], reverse=True))
    team_wins_sorted  = dict(sorted(team_wins.items(), key=lambda item: item[1], reverse=True))
    team_avg_score_sorted  = dict(sorted(team_avg_score.items(), key=lambda item: item[1], reverse=True))

    context = {
        'team_games': team_games_sorted,
        'team_wins': team_wins_sorted,
        'team_avg_score': team_avg_score_sorted,
        'top_team': top_team,
        'top_points': top_points,
    }

    return render(request, 'statistics.html', context)


