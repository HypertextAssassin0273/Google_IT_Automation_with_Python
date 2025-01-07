#!/usr/bin/env python3

import datetime, email, smtplib, sys

def usage():
    print('usage:')
    print('1) python3 send_reminders.py "Date|Meeting Title|Emails"')
    print('2) ./send_reminders.py "Date|Meeting Title|Emails"')
    return 1

def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d") # NOTE: format changed to keep consistency with the input
    return dateobj.strftime("%A")

def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(
        f"Hi all!\n\n"
        f"This is a quick mail to remind you all that we have a meeting about: \"{title}\"\n"
        f"the {weekday} {date}\n\n"
        f"See you there.\n"
    )
    return message

def send_message(message, emails):
    smtp = smtplib.SMTP('localhost', 1025) # NOTE: using debugging server to test emails (since SMTP server is not running on localhost)
    message['From'] = 'noreply@example.com'
    for email in emails.split(','):
        message['To'] = email
        smtp.send_message(message)
        del message['To'] # NOTE: instead of clearing 'To' field before sending the email, it is cleared afterwards to avoid errors
    smtp.quit()

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email with: {}".format(e), file=sys.stderr) # NOTE: error message now gives more context about the failure

if __name__ == '__main__':
    sys.exit(main())


# SIDE-NOTE: use command 'python3 -m smtpd -c DebuggingServer -n localhost:1025' to start a debugging server before running this script
