import imaplib, getpass


class IMAPWrapper:
    """Class to connect to imap server login and extracting emails between two given dates"""
    mail=None
    def __init__(self,username,password):
        try:
            self.mail=imaplib.IMAP4('imap.iitb.ac.in',143)
            self.mail.login(username,password)
            self.mail.select('inbox')
        except:
            print "Wrong Password"
    def get_mails(self,date1,date2):
        msgs=[]
        query = '(SINCE '+date1+' BEFORE '+date2+' )'
        typ,data=self.mail.search(None,query)
        for num in data[0].split():
            head=self.mail.fetch(num,'(RFC822.HEADER)')[1][0]
            msg=self.mail.fetch(num,'(RFC822.TEXT)')[1][0]
            msgs.append([head,msg])
        return msgs

if __name__=="__main__":
    username=raw_input("Username: ")
    password=getpass.getpass()
    date1="14-Aug-2012"
    date2="15-Aug-2012"
    acc = IMAPWrapper(username,password)
    msgs=acc.get_mails(date1,date2)
    print msgs[0]
