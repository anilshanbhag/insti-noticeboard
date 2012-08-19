#!/usr/bin/python
import dateutil.parser
import re

class MailProcessor:
    def __init__(self, message, sender, title):
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
        for line in self.message.split('\n'):
            if "Date" in line or "date" in line:
                self.date = self.clean(line)
            elif "Venue" in line or "venue" in line:
                self.venue = self.clean(line)
            elif "Time" in line or "time" in line:
                self.time = self.clean(line)

        print self.process_date()


    def clean(self ,line):
        return line.strip()

    def process_date(self):
        self.date = re.sub('[\[()\]:-]',' ', self.date)
        self.date = " ".join( self.date.split()[1:] )

        self.time = re.sub('[\[()\]-]',' ', self.time)
        self.time = " ".join( self.time.split()[1:] )

        datestring = self.date + " " + self.time
        date = dateutil.parser.parse(datestring)
        return date

    def process_venue(self):
        pass

if __name__ == "__main__":
    import sample_mail
    processor = MailProcessor(sample_mail.message, sample_mail.sender, sample_mail.title)
