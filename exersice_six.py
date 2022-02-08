import re

# print a list containing only valid email addresses in lexicographical order.


# return True if email is valid, else return False
def check_valid(email: str):

    try:
        print('email:', email)
        username, url = email.split("@")
        print('username:', username)
        print('url:', url)
        website, extension = url.split(".")
        print('website:', website)
        print('extension:', extension)
    except ValueError:
        return False

    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True


def filter_mail(mails):
    return list(filter(check_valid, mails))


number_emails = int(input('Enter the number of email addresses:'))
emails = []
for item in range(number_emails):
    emails.append(input(f'Enter email {item+1}:'))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

