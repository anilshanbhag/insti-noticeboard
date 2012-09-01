# TODO : Change it to use Flask

from config import *
from IMAP import IMAPWrapper
from processor import MailProcessor

def main():
    imap = IMAPWrapper(username, password)
    msgs = imap.get_mails("1-Aug-2012", "15-Aug-2012")
    for msg in msgs:
        processor = MailProcessor(msg[0], msg[1], msg[2] )

main()

