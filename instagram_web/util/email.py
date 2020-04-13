import os
from flask import request
import requests

def send_message():
    print('sending email')
    return requests.post(
        "https://api.mailgun.net/v3/"+os.environ.get("MAILGUN_DOMAIN")+"/messages",
        auth=("api", os.environ.get('MAILGUN_PRIVATE_API_KEY')),
        data={"from": "Excited User <garoad91@gmail.com>",
              "to": ["garoad91@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!",
              "html":"<h3>Hellow World!</h3>"})
