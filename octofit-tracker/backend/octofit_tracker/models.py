from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    class Meta:
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        db_table = 'workouts'