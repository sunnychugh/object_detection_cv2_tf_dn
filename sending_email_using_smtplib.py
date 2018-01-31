import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
#server.connect("smtp.gmail.com", 25)
server.ehlo()
server.starttls()
server.ehlo()
server.login("sunny......@gmail.com", "give_password")

#sender = 'sunny.....@gmail.com'
#receivers = ['sunny.ch.....@city.ac.uk']
#
#message = """From: sunny-gmail <sunny.....@gmail.com>
#To: sunny-city <sunny.ch....@city.ac.uk>
#Subject: --new video detected--
#
#Check the new video."""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


fromaddr = "sunny......@gmail.com"
toaddr = "sunny.ch.....@city.ac.uk"


def attached_text_and_image(image):
    msg = MIMEMultipart()
    msg['From'] = fromaddr 
    msg['To'] = toaddr
    body = "Check the new video."
    msg.attach(MIMEText(body, 'plain'))
    msg['Subject'] = "--new video detected--"

    #msgAlternative = MIMEMultipart('alternative')
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere are the links you wanted:\n\nwindows-dell:   192.168.0.70:5000\nor\nrasp-pi:            192.168.0.85:5000"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?\n<br>
           Here is the <a href="https://abcxyz.localtunnel.me"> global streaming link using localtunnel</a> 
        </p>
      </body>
    </html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    with open(image, 'rb') as fp:
        img = MIMEImage(fp.read())    
    msg.attach(img)

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)


def quit_server():
    server.quit()
