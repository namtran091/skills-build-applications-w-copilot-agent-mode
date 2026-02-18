from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', universe='Marvel')
        self.user = User.objects.create(email='tony@stark.com', name='Tony Stark', team=self.team)
        self.workout = Workout.objects.create(name='Super Strength', description='Strength training for heroes')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2024-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_user(self):
        self.assertEqual(self.activity.user.email, 'tony@stark.com')

    def test_leaderboard_team(self):
        self.assertEqual(self.leaderboard.team.name, 'Marvel')

    def test_workout_name(self):
        self.assertEqual(self.workout.name, 'Super Strength')
