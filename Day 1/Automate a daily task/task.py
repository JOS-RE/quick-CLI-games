import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("sender email address", "sender password")
server.sendmail("sender email address",
                "receiver email address",
                "Enter the mail message here")

server.quit()
