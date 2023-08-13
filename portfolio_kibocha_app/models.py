from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

# Define your choices for the project status
DESIGNING = 'designing'
DEVELOPING = 'developing'
TESTING = 'testing'
DEPLOYING = 'deploying'
LIVE = 'live'
ACQUIRED = 'acquired'
PUBLIC = 'public'
PRIVATE = 'private'

PROJECT_STATUS_CHOICES = [
    (DESIGNING, 'Designing'),
    (DEVELOPING, 'Developing'),
    (TESTING, 'Testing'),
    (DEPLOYING, 'Deploying'),
    (LIVE, 'Live'),
    (ACQUIRED, 'Acquired'),
]

GITHUB_STATUS_CHOICES = [
    ('public', 'Public'),
    ('private', 'Private'),
]


# Define your project model
class Project(models.Model):
    logo = models.ImageField(upload_to='project_logos/')
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES, default=DESIGNING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateField(default=date.today)  # Add the creation_date field
    acquired_date = models.DateField(blank=True, null=True)
    developers = models.CharField(max_length=100, default='John Kibocha')
    progress = models.PositiveIntegerField(default=10, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])  # Default progress set to 10%
    cost = models.PositiveIntegerField(default=20000)
    website = models.URLField(default="", blank=True, null=True)
    source_code = models.URLField(default="https://github.com")
    github_status = models.CharField(max_length=10, choices=GITHUB_STATUS_CHOICES, default='private')

    def __str__(self):
        return self.description


class Review(models.Model):
    profile_photo = models.ImageField(blank=True, null=True, upload_to='review_images',
                                      default='review_images/default_user.png')
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_position = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Milestone(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Skill(models.Model):
    # A skill has a name, a learning progress, a list of projects and a list of tools
    name = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)  # A percentage of 100
    projects = models.JSONField()  # A list of dictionaries with keys 'name' and 'url'
    tools = models.JSONField()  # A list of strings

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200, blank=True)
    company_address = models.CharField(max_length=200, blank=True)
    company_position = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    SUBJECT_CHOICES = [
        ('Request Source Code', 'Request Source Code'),
        ('Reach Out', 'Reach Out'),
        ('Request Resume', 'Request Resume'),
        ('Collaborate', 'Collaborate'),
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
