from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings
from pymongo import MongoClient

# Sample data for superheroes and teams
USERS = [
    {"name": "Clark Kent", "email": "superman@dc.com", "team": "DC"},
    {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "DC"},
    {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Steve Rogers", "email": "captainamerica@marvel.com", "team": "Marvel"},
    {"name": "Natasha Romanoff", "email": "blackwidow@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel", "description": "Marvel Superheroes"},
    {"name": "DC", "description": "DC Superheroes"},
]

ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "Flying", "duration": 120},
    {"user_email": "batman@dc.com", "activity": "Martial Arts", "duration": 90},
    {"user_email": "ironman@marvel.com", "activity": "Engineering", "duration": 60},
]

LEADERBOARD = [
    {"team": "Marvel", "points": 300},
    {"team": "DC", "points": 250},
]

WORKOUTS = [
    {"name": "Strength Training", "description": "Full body workout"},
    {"name": "Cardio", "description": "Endurance workout"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient("mongodb://localhost:27017")
        db = client["octofit_db"]

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Create unique index on email for users
        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
