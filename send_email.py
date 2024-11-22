import os
import logging
import auth
from dotenv import load_dotenv
from base64 import urlsafe_b64decode, urlsafe_b64encode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

load_dotenv()
sender_email = os.getenv("SENDER_EMAIL")



def build_message(destination, obj, body, attachments=[]):
    """
    Builds an email message, either plain text or with attachments.

    Parameters:
    destination (str): The recipient's email address.
    obj (str): The subject of the email.
    body (str): The body of the email message.
    attachments (list): A list of file paths to be attached to the email (optional).

    Returns:
    dict: A dictionary containing the raw base64-encoded email.
    """
    try:
        if not attachments:  # no attachments given
            message = MIMEText(body)
            message["to"] = destination
            message["from"] = sender_email
            message["subject"] = obj

        return {"raw": urlsafe_b64encode(message.as_bytes()).decode()}
    except Exception as e:
        logging.error(f"Error occured in build_message:{e}")


def send_message(service, destination, obj, body, attachments=[]):
    """
    Sends an email message using the Gmail API.

    Parameters:
    service (obj): The Gmail API service object.
    destination (str): The recipient's email address.
    obj (str): The subject of the email.
    body (str): The body of the email.
    attachments (list): A list of file paths to be attached to the email (optional).

    Returns:
    dict: The Gmail API response after the email is sent.
    """
    try:
        return (
            service.users()
            .messages()
            .send(userId="me", body=build_message(destination, obj, body, attachments))
            .execute()
        )
    except Exception as e:
        logging.error(f"Error occured in send_message:{e}")


def send_email(recipient, subject, body):
    """
    Authenticates with Gmail and sends an email.

    Parameters:
    subject (str): The subject of the email.
    body (str): The body of the email message.
    recipient (str): The recipient's email address.

    Returns:
    None
    """
    try:
        # get the Gmail API service
        service = auth.gmail_authenticate()

        send_message(service, recipient, subject, body)
        print("Email Sent!") 
    except Exception as e:
        logging.error(f"Error occured in send_email:{e}")