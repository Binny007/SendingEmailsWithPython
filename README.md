# SendingEmailsWithPython

--> In this project we are using python bulit-in 'email' module for sending emails.
--> Imagine you have a list of emails that you have collected for your new startup and you want people to know about your startup, right? So we can create a program that sends custom emails with their names to maybe hundreds or thousands of people at the same time.
--> Another package we use in this project is 'smtplib'.
--> smtp allow us to create smtp server.
--> Another built-in package we used is 'Template' --> this package will substitute variable inside of text which have '$'
--> Then we use another built-in package called 'pathlib.Path' to read the HTMLfile(index.html), convert it to a template and substitute it 


--> n.b: While running above code, you may get an smtplib.SMTPAuthenticationError. This is because, google blocks your app because of their new policy which wont trust your app to get access to gmail.

--> So to solve this problem, go to Google Account--> Security--> Turn on 2-step verification 
--> Then in App Passwords --> Create new --> Enter App name as 'Python'--> Create --> So you get a new app password and use that password in 'smtp.login()'.
