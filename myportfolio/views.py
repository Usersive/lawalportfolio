import datetime
from django.shortcuts import get_object_or_404, render, redirect
import threading
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
import requests
from  app.forms import EmailForm, SubscriptionForm
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from app.models import About, Client, Content, Experience, File, Profile, Service, Skill, SocialLinks, Testimonial, UnsubscribedUser, Subscriber, Introduction
import os
from django.conf import settings
from django.utils.timezone import now
from django.core.mail import EmailMultiAlternatives
from app.models import SentEmail
import cloudinary.utils

def current_year(request):
    year = datetime.now().year
    return render(request, 'index.html', {'current_year': current_year})

def send_email_in_thread(subject, html_message, sender_email, recipient_list):
    # Convert HTML to plain text
    plain_message = strip_tags(html_message)
    thread = threading.Thread(target=send_mail, args=(subject, plain_message, sender_email, recipient_list),
                              kwargs={'html_message': html_message})
    thread.start()



def email_compose(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['sender_name']
            sender_email = form.cleaned_data['sender_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Render HTML email template
            html_message = render_to_string('app/email_template.html', {
                'sender_name': sender_name,
                'sender_email': sender_email,
                'subject': subject,
                'message': message
            })

            # Send email in a thread
            send_email_in_thread(subject, html_message, sender_email, ['horenteam@gmail.com'])

            # Save email details to the database
            SentEmail.objects.create(
                sender_name=sender_name,
                sender_email=sender_email,
                subject=subject,
                message=message
            )

            messages.success(request, "Message sent successfully and saved!")
            return redirect('/')
    else:
        form = EmailForm()

    return render(request, 'index.html', {'form': form})



def index(request):
    # files = File.objects.first() 
    files = File.objects.all() # Get the only available file
    client= Client.objects.all()
    form = SubscriptionForm()
    profile = Profile.objects.first() 
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    about = About.objects.first()
    intro = Introduction.objects.first()
    testimonial = Testimonial.objects.all()
    service = Service.objects.all()
    link = SocialLinks.objects.all()
    section = request.GET.get('section', 'ALL')
    
     # Generate signed Cloudinary URLs for each file
    for file_obj in files:
        file_obj.signed_url, _ = cloudinary.utils.cloudinary_url(
            file_obj.file.name, secure=True, sign_url=True
        )
    
    
    if section == 'ALL' or not section:
        contents = Content.objects.all()
    else:
        contents = Content.objects.filter(section=section)
    
    
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, "You're already subscribed!")
            else:
                form.save()
                messages.success(request, "Subscription successful!")
            return redirect('index')  # Redirect to clear the form
    context ={
        'form': form,
        'files': file_obj,
        'clients': client,
        'profiles': profile,
        'experiences': experience,
        'skills': skill,
        'abouts': about,
        'introductions':intro,
        'testimonies': testimonial,
        'services': service,
        'contents': contents,
        'links':link,
    }
    return render(request, 'index.html', context)



def download_file(request, file_id):
    try:
        file_obj = get_object_or_404(File, id=file_id)

        # Cloudinary URL
        file_url = file_obj.file.url  # This should return the Cloudinary URL
        print(file_obj.file.url)

        # Redirect to the Cloudinary URL for the file
        return HttpResponseRedirect(file_url)

    except File.DoesNotExist:
        raise Http404("File not found")




def subscribe_newsletter(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if email exists in UnsubscribedUser
            if UnsubscribedUser.objects.filter(email=email).exists():
                return JsonResponse({"message": "You have previously unsubscribed. Contact support to resubscribe."}, status=400)

            subscriber, created = Subscriber.objects.get_or_create(email=email)

            if not created:
                return JsonResponse({"message": "You're already subscribed!"}, status=400)
            else:
                # Send confirmation email
                unsubscribe_url = request.build_absolute_uri(reverse('unsubscribe', args=[subscriber.unsubscribe_token]))
                html_content = render_to_string("app/subscription_email.html", {'unsubscribe_link': unsubscribe_url})
                text_content = strip_tags(html_content)

                email_message = EmailMultiAlternatives(
                    subject="Subscription Confirmation",
                    body=text_content,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[email]
                )
                email_message.attach_alternative(html_content, "text/html")
                email_message.send()

                return JsonResponse({"message": "Subscription successful! A confirmation email has been sent."})

    return JsonResponse({"message": "Invalid request."}, status=400)


def unsubscribe(request, token):
    subscriber = Subscriber.objects.filter(unsubscribe_token=token).first()

    if not subscriber:
        messages.error(request, "Invalid or expired unsubscribe link.")
        return redirect('index')  # Redirect to homepage

    email = subscriber.email  # Store email before removing from subscribers list

    # Move user to the UnsubscribedUser table
    UnsubscribedUser.objects.create(email=email, unsubscribed_at=now())

    # Remove from subscribers list
    subscriber.delete()

    # Send Unsubscribe Confirmation Email
    subject = "You Have Unsubscribed"
    html_content = render_to_string("app/unsubscribe_email.html", {"email": email})
    text_content = strip_tags(html_content)  # Plain text fallback

    email_message = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()

    messages.success(request, "You have successfully unsubscribed. A confirmation email has been sent.")
    return redirect('index')

def favicon_view(request):
    """Manually serve favicon.ico"""
    favicon_path = os.path.join(settings.BASE_DIR, 'static/logo/favicon.ico')
    if os.path.exists(favicon_path):
        return FileResponse(open(favicon_path, "rb"), content_type = "image/x-icon")
    return HttpResponse(status=404)