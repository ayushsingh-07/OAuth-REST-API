# -*- encoding: utf-8 -*-

"""Password Security with MD5"""

import os
import hashlib
import smtplib

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True)

def encrypt(_password : str) -> str:
    """Encrypts the Password with MD5 and SALT"""
    __password_salt__ = os.getenv('forward_salt') + _password + os.getenv('backward_salt')
    return hashlib.sha256(__password_salt__.encode()).hexdigest()

def validate(_password : str, _original_password : str) -> bool:
    """Validate Password"""
    __password_salt__ = os.getenv('forward_salt') + _password + os.getenv('backward_salt')
    
    if hashlib.sha256(__password_salt__.encode()).hexdigest() == _original_password:
        return True

    return False

class Mailing(object):
    """Email Sending Class"""

    def __init__(self, protocol : str = "SMTP", **kwargs):
        """default constructor"""

        self.protocol    = protocol # only SMTP setup completed

        # set SMTP
        self._host = os.getenv("MAIL_SMTP_SERVER")
        self._port = os.getenv("MAIL_SMTP_SERVER_PORT")

        self.mail_server = smtplib.SMTP(
                host = self._host,
                port = self._port
            )

        # login to the email server
        self._login() 

    def _login(self):
        # check login
        self.mail_server.login(
                user     = os.getenv("ADMIN_EMAIL"),
                password = os.getenv("ADMIN_EMAIL_PASSWORD"),
            )

        return True

    def _close(self):
        # close server
        self.mail_server.quit()

    def __str__(self):
        return f"{__name__}: PROTOCOL = {self.protocol}"

    def __repr__(self):
        return f"{__name__}: PROTOCOL = {self.protocol} ({self._host}, {self._port})"

if __name__ == "__main__":
    # check if email is working
    # run this code using `python utils.py`
    obj = Mailing()
    print(obj, repr(obj))

    try:
        obj._login()
    except Exception as err:
        raise ValueError("Email Not Working", err)
    finally:
        obj._close()

    print("success")