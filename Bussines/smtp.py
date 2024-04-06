import smtplib
from email.message import EmailMessage

def createMsg(message, subject, sender, destinatary):
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = destinatary

    return msg

def sendMsg(msgPrepared):
    #smtp.googlemail.com
    #smtp.gmail.com
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(msgPrepared['From'], "zupb hato tfeu jkkv")
    s.send_message(msgPrepared)
    s.quit()
    print(f"Message sended: {msgPrepared}")