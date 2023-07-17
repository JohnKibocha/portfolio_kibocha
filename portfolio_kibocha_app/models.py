from django.db import models

# Create your models here.

# Define your choices for the project status
DESIGNING = 'designing'
DEVELOPING = 'developing'
TESTING = 'testing'
DEPLOYING = 'deploying'
LIVE = 'live'
ACQUIRED = 'acquired'

PROJECT_STATUS_CHOICES = [
    (DESIGNING, 'Designing'),
    (DEVELOPING, 'Developing'),
    (TESTING, 'Testing'),
    (DEPLOYING, 'Deploying'),
    (LIVE, 'Live'),
    (ACQUIRED, 'Acquired'),
]


# Define your project model
class Project(models.Model):
    logo = models.ImageField(upload_to='project_logos/')
    # Remove the status_icon field, as it is no longer needed
    # status_icon = models.ImageField(upload_to='project_status_icons/')
    # Define your project status field with the choices option
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES, default=DESIGNING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    acquired_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.description


class Review(models.Model):
    profile_photo = models.ImageField(blank=True, null=True, upload_to='review_images', default='default_user.png')
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_position = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Milestone(models.Model):
    date_range = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.description

