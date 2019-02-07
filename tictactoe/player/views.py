from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import InvitationForm
from .models import Invitation
from gameplay.models import Game

# Create your views here.
@login_required
def home(request):
  my_games = Game.objects.games_for_user(request.user)
  active_games = my_games.active()

  return render(request, "player/home.html", {
    'games': active_games
  })

@login_required
def new_invitation(request):
  if request.method == "POST":
    invitation = Invitation(from_user=request.user)
    form = InvitationForm(instance=invitation, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('player_home')
  else:
    form = InvitationForm()
  return render(request, "player/new_invitation_from.html", {'form': form})
