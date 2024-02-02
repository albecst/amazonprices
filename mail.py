import smtplib

def sendemail(message):
    email = "popotemerengote69@gmail.com"
    password = "L33resdecrack$321!"
    send_to_email = "albertocastilloAC05@gmail.com"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, send_to_email, message)
    server.quit()