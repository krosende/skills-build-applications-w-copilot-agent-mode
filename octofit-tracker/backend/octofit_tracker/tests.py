from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(str(team), "Test Team")

    def test_user_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass", team=team)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.team, team)

    def test_activity_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass", team=team)
        activity = Activity.objects.create(user=user, type="run", duration=30, calories=200)
        self.assertEqual(activity.type, "run")

    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")

    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass", team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
