import re


def find_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)


text = """
Hello everyone!

You can contact Khushi at:
khushi@gmail.com
khushi123@college.edu
support@example.org
invalid-email@com
khushi.shinde@domain.co.in

Thank you!
"""

emails = find_email_addresses(text)

print("Email addresses found:")
if emails:
    for email in emails:
        print(email)
else:
    print("No email addresses were found.")

print("\nTotal emails found:", len(emails))