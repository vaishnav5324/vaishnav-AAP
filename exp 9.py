mport re

text = "Contact me at abc@gmail.com or test123@yahoo.com"

email_pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}"

emails = re.findall(email_pattern, text)
print("--Email found--")

for email in emails:
    print(email)
