from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Project, Review, Milestone


# Create your views here.
def index_page(request):
    user_review = Review.objects.all()
    recent_projects = Project.objects.order_by('-acquired_date')[:9]
    context = {'projects': recent_projects, 'reviews': user_review}
    return render(request, 'index.html', context)


def profile_page(request):
    major_milestones = Milestone.objects.order_by('-date_range')[:5]
    return render(request, "profile.html", {'milestones': major_milestones})


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
