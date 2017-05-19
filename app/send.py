import smtplib

def send(sender, name, email,subject, message):
   packet= """From: {} <{}>\nTo: {} \nSubject: {}\n{}"""
   packet_sent= packet.format(name,sender,email,subject,message)
   server = smtplib.SMTP('localhost')
   server.starttls()
   server.sendmail(sender, email, packet_sent)
   server.quit()
   return