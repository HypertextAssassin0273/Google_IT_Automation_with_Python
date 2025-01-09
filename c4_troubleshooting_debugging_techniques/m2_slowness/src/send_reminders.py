#!/usr/bin/env python3

import datetime, email, smtplib, sys, csv

def usage():
    print('usage:')
    print('1) python3 send_reminders.py "Date|Meeting Title|Emails"')
    print('2) ./send_reminders.py "Date|Meeting Title|Emails"')
    return 1

def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d") # NOTE: format changed to keep consistency with the input
    return dateobj.strftime("%A")

def message_template(date, title, name):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(
        f"Hi {name}!\n\n"
        f"This is a quick mail to remind you all that we have a meeting about: \"{title}\"\n"
        f"the {weekday} {date}\n\n"
        f"See you there.\n"
    )
    return message

def read_names(contacts): # NOTE: optimized to read names faster via dictionary
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip header row
        for row in reader:
            names[row[0]] = row[1] # email is used as key to avoid duplicates
    return names

def send_message(date, title, emails, names):
    smtp = smtplib.SMTP('localhost', 1025) # NOTE: using debugging server to test emails (since SMTP server is not running on localhost)
    for email in emails.split(','):
        name = names.get(email, 'Friend') # NOTE: search for name using email as key in O(1) time
        message = message_template(date, title, name)
        message['From'] = 'noreply@example.com'
        message['To'] = email
        smtp.send_message(message)
        del message['To'] # NOTE: clear the 'To' field after sending the email to avoid reusing the older recipient
    smtp.quit()

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        names = read_names('contacts.csv') # NOTE: read names only once, SIDE-NOTE: ensure .csv file is present with correct order of fields
        send_message(date, title, emails, names)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email with: {}".format(e), file=sys.stderr) # NOTE: error message now gives more context about the failure

if __name__ == '__main__':
    sys.exit(main())


# SIDE-NOTE: use command 'aiosmtpd -n -l :1025' to start a debugging server before running this script
