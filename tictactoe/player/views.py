from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import InvitationForm
from .models import Invitation
from gameplay.models import Game

# Create your views here.
@login_required
def home(request):
  my_games = Game.objects.games_for_user(request.user)
  active_games = my_games.active()
  invitations = request.user.invitations_received.all()
  return render(request, "player/home.html", {
    'games': active_games,
    'invitations': invitations
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

@login_required
def accept_invitation(request, id):
  invitation = get_object_or_404(Invitation, pk=id)
  if not request.user == invitation.to_user:
    raise PermissionDenied
  if request.method == 'POST':
    if "accept" in request.POST:
      game = Game.objects.create(
        first_player=invitation.to_user,
        second_player=invitation.from_user,
      )
      invitation.delete()
      return redirect('player_home')
  else:
    return render(request,
      "player/accept_invitation_form.html",
      {'invitation': invitation}
    )
