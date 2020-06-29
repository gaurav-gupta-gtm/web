import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("g.gupta1728@gmail.com", "raqu7964HKL") 
# message to be sent 
message = "Hey Developer,Our website is up."
# sending the mail 
s.sendmail("itzme485@gmail.com", "g.gupta1728@gmail.com", message) 
# terminating the session 
s.quit()
