import flask
import functions_framework
import os
import logging
import requests

@functions_framework.http
def sendEmail(request: flask.Request) -> flask.typing.ResponseReturnValue:
    logging.info("{} request received".format(request.method))
    request_json = request.get_json()
    
    if request_json:
        logging.info("Request JSON: {}".format(request_json))
    
    if request.method == "POST":
        try: 
            requests.post(
                "https://api.mailgun.net/v3/mail.patricksaul.com/messages",
                auth=("api", os.environ.get("MAILGUN_API_KEY")),
                data={
                    "from": "Patricksaul.com Mail <mailgun@mail.patricksaul.com>",
                    "to": "Patrick Saul <patricksaul20@gmail.com>",
                    "subject": request_json["subject"],
                    "text": request_json["text"],
                },
                timeout=5,
            )
            logging.info("Email sent")
            return "Email sent", 200
        except Exception as e:
            logging.error("Error sending email: {}".format(e))

