from django.shortcuts import render, redirect
from .models import Project, Review
from .forms import ReviewForm


# Create your views here.
def index_page(request):
    user_review = Review.objects.all()
    recent_projects = Project.objects.order_by('-acquired_date')[:9]
    context = {'projects': recent_projects, 'reviews': user_review}
    return render(request, 'index.html', context)


def profile_page(request):
    return render(request, 'profile.html')


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
