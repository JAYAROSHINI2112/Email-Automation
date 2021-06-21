import csv
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "kamaldgrt@gmail.com"
password = "" # Add the app specific password here

message = MIMEMultipart("alternative")
message["Subject"] = "Multiple Email Testing Part 3"
message["From"] = sender_email
message["To"] = sender_email

def content(name, email):
    html = "<html>"
    html += "<body>"
    html += "<p>Hi, <b>" + name + "</b><br>"
    html += "How are you?<br>"
    html += "I think your email id is: " + email + "<br>"
    html +=  "Your Grade is : " 
    html += "</p></body></html>"
    return html


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)


    with open("test.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for receiver, rec_email in reader:
            print(f"Sending email to {receiver}, {rec_email}")
            htmlcontent = content(receiver, rec_email)
            htmlpart = MIMEText(htmlcontent, "html")
            message.attach(htmlpart)
            server.sendmail(
                sender_email, rec_email, message.as_string()
            )
