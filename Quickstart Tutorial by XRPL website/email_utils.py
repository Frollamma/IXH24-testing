import os
from mailjet_rest import Client
from dotenv import load_dotenv

load_dotenv()

def create_email_content(wallet):
    """
    Create the content of the email for the NFT wallet details.
    """
    email_body = f"""
    Hello,

    Your new NFT wallet has been successfully created. Here are your wallet details:

    **Address**: {wallet.address}
    **Seed**: {wallet.seed}

    Please keep these credentials secure as they grant full access to your wallet.

    Best regards,
    The DIADEN team
    """
    return email_body

def send_email(subject, recipient_email, sender_email, wallet):
    """
    Send an email using Mailjet.
    """
    # Mailjet API credentials
    api_key = os.getenv("MAILJET_API_KEY")
    api_secret = os.getenv("MAILJET_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("Mailjet API credentials are not set in the environment variables.")

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    body = create_email_content(wallet=wallet)
    data = {
        'Messages': [
            {
                "From": {
                    "Email": sender_email,
                    "Name": "DIADEN"
                },
                "To": [
                    {
                        "Email": recipient_email
                    }
                ],
                "Subject": subject,
                "TextPart": body
            }
        ]
    }

    result = mailjet.send.create(data=data)
    # id = result.json()['Messages'][0]['MessageID']
    # result = mailjet.message.get(id=id)
    # print(result.status_code)
    # print(result.json())
    if result.status_code != 200:
        raise Exception(f"Failed to send email: {result.json()}")
    return result.json()
