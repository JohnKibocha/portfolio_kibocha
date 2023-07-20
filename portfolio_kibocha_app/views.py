from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Project, Review, Milestone, Skill
from django.core.paginator import Paginator, EmptyPage


# Create your views here.
def index_page(request):
    user_review = Review.objects.all()
    recent_projects = Project.objects.order_by('-acquired_date')[:9]
    context = {'projects': recent_projects, 'reviews': user_review}
    return render(request, 'index.html', context)


def profile_page(request):
    milestones = Milestone.objects.all()
    skills = Skill.objects.all()
    # Number of items per page (in this case, 10)
    items_per_page = 10

    paginator = Paginator(milestones, items_per_page)
    page_number = request.GET.get('page')

    try:
        page_number = int(page_number) if page_number else 1
        milestones = paginator.page(page_number)
    except (ValueError, EmptyPage):
        return HttpResponseBadRequest("Invalid page number")

    return render(request, "profile.html", {'milestones': milestones, 'skills': skills})


def blogs_page(request):
    return render(request, 'blogs.html')


def contact_me_page(request):
    return render(request, 'contact-me.html')


def portfolio_page(request):
    return render(request, 'portfolio.html')


def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form})


def thankyou_page(request):
    return render(request, 'thankyou.html')


