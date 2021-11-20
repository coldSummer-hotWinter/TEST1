import re

strDate = 'June 24, August 9, Dec 12'
reg = r"[a-zA-Z]+ \d+"
matches = re.findall(reg, strDate)
for match in matches:
    print(match)
