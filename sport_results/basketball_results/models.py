from django.db import models

class BasketballMatch(models.Model):
    match = models.CharField(max_length=100)
    date = models.DateField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    score1 = models.IntegerField()
    score2 = models.IntegerField()

    def __str__(self):
        return f'{self.team1} {self.score1} - {self.score2} {self.team2}'



