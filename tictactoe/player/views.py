from django.shortcuts import render

from gameplay.models import Game

# Create your views here.
def home(request):
  return render(request, "player/home.html", {
    'ngames': Game.objects.count()
  })