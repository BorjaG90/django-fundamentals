from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class Game(models.Model):
  first_player = models.ForeignKey(User,
    related_name="games_first_player", on_delete=models.CASCADE)
  second_player = models.ForeignKey(User,
    related_name="games_second_player", on_delete=models.CASCADE)
  start_time = models.DateTimeField(auto_now_add=True)
  last_active = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=1, default='F')

  def __str__(self):
    return "{0} vs {1}".format(
      self.first_player, self.second_player
    )

class Move(models.Model):
  x = models.IntegerField()
  y = models.IntegerField()
  comment = models.CharField(max_length=300, blank=True)
  by_first_player = models.BooleanField()

  game = models.ForeignKey(Game, on_delete=models.CASCADE)
