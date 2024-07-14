from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hey I am jango server</h1>")


def success_page(request):
    return HttpResponse("<h1>Hey I am this is success</h1>")

# views.py

# views.py
# views.py

# views.py

from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.mail import BadHeaderError

def send_test_email_with_attachment(request):
    subject = 'Python (Selenium) Assignment sumeet khatri'
    message = 'This is a test email sent from a Django application with an attachment.'
    email_from = 'khatrisumeet400@gmail.com'
    recipient_list = ['tech@themedius.ai']
    cc_list = ['hr@themedius.ai']
    attachment_file_path = 'C:\\Users\\admin\\Desktop\\coreimg\\image.png'

    email = EmailMessage(subject, message, email_from, recipient_list, cc_list)
    
    try:
        with open(attachment_file_path, 'rb') as f:
            email.attach('image.png', f.read(), 'image/png')
        email.send()
    except BadHeaderError:
        return HttpResponseBadRequest('Invalid header found.')
    except Exception as e:
        return HttpResponseBadRequest(f'An error occurred: {str(e)}')
    
    return HttpResponse('Email with attachment sent successfully')




