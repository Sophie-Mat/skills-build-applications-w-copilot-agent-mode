from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        
        # Ensure users are saved before assigning them to teams
        for user in users:
            user.save()

        # Create teams and assign members using the set() method
        teams = [
            Team(name='Blue Team'),
            Team(name='Gold Team'),
        ]
        
        # Save teams and assign members using the set() method
        for team in teams:
            team.save()

        # Assign members to teams after saving users
        teams[0].members.set(User.objects.filter(email__in=['thundergod@mhigh.edu', 'metalgeek@mhigh.edu', 'zerocool@mhigh.edu']))
        teams[1].members.set(User.objects.filter(email__in=['crashoverride@mhigh.edu', 'sleeptoken@mhigh.edu']))

        # Create activities
        activities = [
            Activity(user=User.objects.get(email='thundergod@mhigh.edu'), type='Cycling', duration=60, date='2025-04-08'),
            Activity(user=User.objects.get(email='metalgeek@mhigh.edu'), type='Crossfit', duration=120, date='2025-04-07'),
            Activity(user=User.objects.get(email='zerocool@mhigh.edu'), type='Running', duration=90, date='2025-04-06'),
            Activity(user=User.objects.get(email='crashoverride@mhigh.edu'), type='Strength', duration=30, date='2025-04-05'),
            Activity(user=User.objects.get(email='sleeptoken@mhigh.edu'), type='Swimming', duration=75, date='2025-04-04'),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], points=100),
            Leaderboard(team=teams[1], points=90),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))