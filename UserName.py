import re
name = input("Enter your Name: ")
givenString = "Hello <<UserName>>, How are you?"
requiredString = re.sub("<<UserName>>", name, givenString)
print(requiredString)