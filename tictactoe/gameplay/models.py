from django.db import models

# Create your models here.

class Game(models.Model):
  first_player = models.ForeignKey(User,
                                    related_name="games_first_player")
  second_player = models.ForeignKey(User,
                                    related_name="games_second_player")
  start_time = models.DateTimeField(auto_now=True)
  last_active = models.DateTimeField(auto_now=True)

class Move(models.Model):
  x = models.IntegerField()
  y = models.IntegerField()
  comment = models.CharField(max_length=300, blank=True)
  by_first_player = models.BooleanField()