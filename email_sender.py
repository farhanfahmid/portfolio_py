import smtplib #for email
import ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "fahmidfarhan274@gmail.com"
    password = "dwfe wpzg xokv pzxd"
    receiver = "fahmidfarhan274@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


