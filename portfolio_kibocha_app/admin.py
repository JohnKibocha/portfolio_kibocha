from django.contrib import admin
from .models import Project, Review, Milestone, Skill

# Register your models here.
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Milestone)
admin.site.register(Skill)

