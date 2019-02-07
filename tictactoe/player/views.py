from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from gameplay.models import Game

# Create your views here.
@login_required
def home(request):
  my_games = Game.objects.games_for_user(request.user)
  active_games = my_games.active()

  return render(request, "player/home.html", {
    'games': active_games
  })