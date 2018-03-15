#  Django mail module this will be responsible for sending the emails
from django.core.mail import EmailMultiAlternativesclass

from django.template.loader import render_to_string
# a function that takes in a name and a receiver email
def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the instagram,you have successfully registered your account'
    sender = 'evanmwenda@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()