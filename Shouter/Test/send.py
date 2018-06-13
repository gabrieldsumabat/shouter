from flask import Flask
from flask_mail import Mail, Message
import os
 
app = Flask(__name__)
 
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": int(465),
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'sixbeforethirty@gmail.com' ,
    "MAIL_PASSWORD": 'SeekTheDao3'
}
 
app.config.update(mail_settings)
mail = Mail(app)


if __name__ == '__main__':
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["gabrieldsumabat@gmail.com"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)