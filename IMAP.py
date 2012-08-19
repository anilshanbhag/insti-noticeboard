import imaplib, email


class IMAPWrapper:
    """
    Class to connect to imap server login and extracting emails
    between two given dates
    """

    def __init__(self,username,password):
        try:
            self.mail=imaplib.IMAP4('imap.iitb.ac.in',143)
            self.mail.login(username,password)
            self.mail.select('inbox')
        except:
            print "Wrong Password"

    def get_mails(self,date1,date2):
        msgs=[]
        query = '(SINCE ' + date1 + ' BEFORE ' + date2 + ' TO "events@iitb.ac.in" )'
        typ,data=self.mail.search(None,query)
        for num in data[0].split():
            msg=self.mail.fetch(num,'(RFC822)')
            msg=email.message_from_string(msg[1][0][1])
            body=""
            for part in msg.walk():
            	if part.get_content_type() == 'text/plain':
            		body="\n" + part.get_payload() + "\n"
            msgs.append([msg['From'],msg['Subject'],body])
        return msgs

if __name__=="__main__":
    username=raw_input("Username: ")
    password=raw_input("Password: ")
    date1="1-Aug-2012"
    date2="15-Aug-2012"
    acc = IMAPWrapper(username,password)
    msgs=acc.get_mails(date1,date2)
    print msgs[0]
