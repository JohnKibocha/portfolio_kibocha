from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ReviewForm
from .models import Project, Review, Milestone, Skill, Contact
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q


# Create your views here.
def index_page(request):
    user_review = Review.objects.all()
    recent_projects = Project.objects.order_by('-acquired_date')[:3]
    context = {'projects': recent_projects, 'reviews': user_review}
    return render(request, 'index.html', context)

#
# def search(request):
#     query = request.GET.get('q')  # Get the search query from the request
#
#     # Perform the search using Q objects
#     project_results = Project.objects.filter(
#         Q(name__icontains=query) | Q(description__icontains=query)
#     )
#
#     skill_results = Skill.objects.filter(
#         Q(name__icontains=query) | Q(tools__icontains=query)
#     )
#
#     context = {
#         'query': query,
#         'project_results': project_results,
#         'skill_results': skill_results,
#     }
#     return render(request, 'search_results.html', context)


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


def portfolio_page(request):
    projects = Project.objects.order_by('creation_date')[:3]
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects, 'projects': projects}
    return render(request, 'portfolio.html', context)


def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form})


def contact_me_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company_name']
        company_address = request.POST['company_address']
        company_position = request.POST['company_position']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            company_address=company_address,
            company_position=company_position,
            email=email,
            phone_number=phone_number,
            subject=subject,
            message=message
        )
        contact.save()

        send_mail(
            f"New Contact: {subject}",  # Subject of the email
            f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}",
            # Email content
            settings.DEFAULT_FROM_EMAIL,  # Sender's email address
            ['johnkibocha@outlook.com'],  # Recipient's email address
            fail_silently=False,
        )

        return redirect('success')  # Redirect to a success page

    return render(request, 'contact-me.html')


def thankyou_page(request):
    return render(request, 'thankyou.html')


def success_page(request):
    return render(request, 'success.html')
