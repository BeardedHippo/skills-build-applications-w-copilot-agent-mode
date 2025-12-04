# populate_db.py
"""
Script om voorbeelddata toe te voegen aan MongoDB via Django models.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Voeg voorbeeld users toe
def populate_users():
    User.objects.create(username='alice', email='alice@example.com', team='Red')
    User.objects.create(username='bob', email='bob@example.com', team='Blue')

# Voeg voorbeeld teams toe
def populate_teams():
    Team.objects.create(name='Red', members=['alice'])
    Team.objects.create(name='Blue', members=['bob'])

# Voeg voorbeeld activiteiten toe
def populate_activities():
    Activity.objects.create(user='alice', type='run', duration=30, calories=250, date='2025-12-01')
    Activity.objects.create(user='bob', type='cycle', duration=45, calories=400, date='2025-12-02')

# Voeg voorbeeld leaderboard toe
def populate_leaderboard():
    Leaderboard.objects.create(team='Red', points=250)
    Leaderboard.objects.create(team='Blue', points=400)

# Voeg voorbeeld workouts toe
def populate_workouts():
    Workout.objects.create(name='Push Ups', description='Do 20 push ups', difficulty='Easy')
    Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='Medium')

if __name__ == "__main__":
    populate_users()
    populate_teams()
    populate_activities()
    populate_leaderboard()
    populate_workouts()
    print("Database succesvol gevuld met voorbeelddata.")
