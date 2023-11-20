from django.shortcuts import render, redirect
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings
from .forms import NewsletterForm


def subscribe_to_newsletter(request):

    api_key = settings.MAILCHIMP_API_KEY
    list_id = settings.MAILCHIMP_LIST_ID

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            mailchimp_client = Client()
            mailchimp_client.set_config({
                'api_key': api_key,
            })

            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user_info = {
                'email_address': email,
                'status': 'subscribed',
                'merge_fields': {
                    'FNAME': first_name,
                    'LNAME': last_name
                }
            }

            try:
                mailchimp_client.lists.add_list_member(list_id, user_info)
                return redirect('success')
            except ApiClientError as error:
                print(error.text)
                return redirect('error')
    else:
        form = NewsletterForm()
    
    context = {
        'form': form
    }

    return render(request, 'mail_chimp.html', context)


def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')
