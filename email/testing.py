import requests
from dotenv import load_dotenv
import os

load_dotenv()


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5b826ca311874f22a138bd525b351d64.mailgun.org/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox5b826ca311874f22a138bd525b351d64.mailgun.org>",
            "to": "Patrick Saul <patricksaul20@gmail.com>",
            "subject": "Hello Patrick Saul",
            "text": "Congratulations Patrick Saul, you just sent an email with Mailgun!  You are truly awesome!",
        },
    )


send_simple_message()
print("Message Sent")


# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.
