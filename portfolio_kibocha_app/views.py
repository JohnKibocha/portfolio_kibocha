from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.http import require_POST
from .forms import ReviewForm
from .models import Project, Review, Milestone, Skill, Contact, Profile


# Create your views here.
def index_page(request):
    user_review = Review.objects.all()
    recent_projects = Project.objects.order_by('-acquired_date')[:3]
    context = {'projects': recent_projects, 'reviews': user_review}
    return render(request, 'index.html', context)


def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Project.objects.filter(name__icontains=query)

    context = {'results': results, 'query': query}
    return render(request, 'search_results.html', context)


def profile_page(request):
    milestones = Milestone.objects.all()
    skills = Skill.objects.all()
    profiles = Profile.objects.all()
    return render(request, "profile.html", {'milestones': milestones, 'skills': skills, 'profile': profiles})


def blogs_page(request):
    return render(request, 'blogs.html')


def portfolio_page(request):
    projects = Project.objects.order_by('creation_date')[:3]
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects, 'projects': projects}
    return render(request, 'portfolio.html', context)


def review_page(request):
    reviews = Review.objects.filter(approved=True)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)  # Added request.FILES argument
        if form.is_valid():
            review = form.save()
            subject = 'New comment from {}'.format(review.name)
            message = 'You have a new comment from {} on your django app. \n\n{}\n\nDo you want to delete or publish this comment? \n\nTo delete, click here: {}\n\nTo publish, click here: {}'.format(
                review.name, review.comment, 'delete_link', 'publish_link')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['kibocha.alerts@gmail.com']

            # Load the HTML template for the email content
            html_content = get_template('review_email_template.html').render({
                'name': review.name,
                'place_of_work': review.place_of_work,
                'job_description': review.job_description,
                'comment': review.comment,
                'created_at': review.created_at,
            })

            # Send the HTML email
            send_mail(subject, message, email_from, recipient_list, html_message=html_content)
            return redirect('thankyou')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form, 'reviews': reviews})


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

        email_subject = request.POST['subject']

        subject = 'New comment from {}'.format(contact.first_name, contact.last_name)
        message = ''
        email_from = 'email'
        recipient_list = ['kibocha.alerts@gmail.com']

        # Load the HTML template for the email content
        html_content = get_template('contact_me_email_template.html').render({
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'email': contact.email,
            'phone_number': contact.phone_number,
            'message': contact.message,
            'created_at': contact.timestamp,
        })

        send_mail(email_subject, message, email_from, recipient_list, html_message=html_content)
        return redirect('success')
    return render(request, 'contact-me.html')


def thankyou_page(request):
    return render(request, 'thankyou.html')


def success_page(request):
    return render(request, 'success.html')
