import re

pattern = r'Hello'

string = 'Hello, World!'

match = re.match(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")
