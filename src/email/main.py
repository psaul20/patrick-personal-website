import flask
import functions_framework
import os
import logging
import requests

@functions_framework.http
def sendEmail(request: flask.Request) -> flask.typing.ResponseReturnValue:
    logging.info("{} request received".format(request.method))
    print("request received")
    
    # For more information about CORS and CORS preflight requests, see:
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request

    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        print("Options Request")
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
        }
        return ("", 204, headers)
    
    # Set CORS headers for the main request
    headers = {"Access-Control-Allow-Origin": "*",
               "Content-Type": "text"}
    
    if request.method == "POST":
        try: 
            request_json = request.get_json()
            if request_json:
                logging.info("Request JSON: {}".format(request_json))
            requests.post(
                "https://api.mailgun.net/v3/mail.patricksaul.com/messages",
                auth=("api", os.environ.get("MAILGUN_API_KEY")),
                data={
                    "from": "Patricksaul.com Mail <mailgun@mail.patricksaul.com>",
                    "to": "Patrick Saul <patricksaul20@gmail.com>",
                    "subject": request_json["subject"],
                    "text": "Sender: {}\nSender Email: {}\n\n{}".format(request_json["sender-name"], request_json["sender-email"], request_json["message-text"]),
                },
                timeout=5,
            )
            logging.info("Email sent")
            return ("", 200, headers)
        except Exception as e:
            logging.error("Error sending email: {}".format(e))
    


