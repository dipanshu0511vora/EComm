from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email , email_token):
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'HI, click on the link to activate your account http://127.0.0.1:8000/Accounts/activate/{email_token}'

    send_mail(subject , message , email_from , [email])

# def send_welcome_email(request):
#     subject = 'Welcome to My Site'
#     message = 'Thank you for creating an account!'
#     from_email = 'admin@mysite.com'
#     recipient_list = [request.user.email]
#     send_mail(subject, message, from_email, recipient_list)
