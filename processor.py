#!/usr/bin/python
import dateutil.parser
import re

class MailProcessor:
    def __init__(self, sender, title, message):
        self.message = message
        self.sender = sender
        self.title = title

        # Details to extract
        self.date = ""
        self.time = ""
        self.venue = ""

        self.event_details()

    def event_type(self, message, sender):
        pass

    def event_details(self):
        self.process_title()
        self.process_message()

        for line in self.message.split('\n'):
            print line
            if "Date" in line or "date" in line:
                self.date = self.clean(line)
            elif "Venue" in line:
                self.venue = self.clean(line)
            elif "Time" in line or "time" in line:
                self.time = self.clean(line)

        print self.date
        print self.venue
        print self.time
        try:
            self.process_date()
            self.process_venue()
        except:
            pass

    def clean(self ,line):
        return line.strip()

    def process_message(self):
        """ Strips events headers from top and bottom of message """
        self.message = "\n".join( self.message.split('\n')[19:-7] )

    def process_date(self):
        self.date = re.sub('[\[()\]:-]',' ', self.date)
        self.date = " ".join( self.date.split()[1:] )

        self.time = re.sub('[\[()\]-]',' ', self.time)
        self.time = " ".join( self.time.split()[1:] )

        datestring = self.date + " " + self.time
        date = dateutil.parser.parse(datestring)
        self.date = date

    def process_venue(self):
        self.venue = " ".join( self.venue.split()[1:] )

    def process_title(self):
        self.title = re.sub('\[.*\]', '', self.title)

if __name__ == "__main__":
    import sample_mail
    processor = MailProcessor(sample_mail.message, sample_mail.sender, sample_mail.title)
