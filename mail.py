import smtplib

def sendemail(message):
    email = "popotemerengote69@gmail.com"
    password = "tfcjofbubaqunxuq"
    send_to_email = "albertocastilloac05@gmail.com"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, send_to_email, message)
    server.quit()