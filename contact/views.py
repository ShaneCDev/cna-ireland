from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse


def contact(request):
    """Contact us page"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm()
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse("Invalid header.")
            return redirect('success')

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    return render(request, 'contact/contact_success.html')
