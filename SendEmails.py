import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#taking credentials
email = input("Enter your e-mail address: \n")
password = input("Enter your password: \n")
senderadd = email
#storing Multiple reciptents addresses
lst = []
reciveradd = lst.append(input("Enter Receiver's email Address: \n"))
msg = MIMEMultipart()
#taking messages
msg['To'] = ",".join(reciveradd)
msg['From'] = senderadd
msg['Subject'] = input("Enter subject: \n")
body = input("Enter Message: \n")t'
msg.attach(MIMEText(body,'plain'))
#connecting to gmail
mail = smtplib.SMTP('smtp.gmail.com',2525)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text = msg.as_string()
mail.sendmail(senderadd,reciveradd,text)
print("Sent!")
mail.quit()
