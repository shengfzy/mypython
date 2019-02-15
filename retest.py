import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'a', lambda m:'['+m.group(0)+']', text,0))