
import re

string = input()

regex = r'[a-zA-Z]+[\w.]*@[a-zA-Z]+\.[a-zA-Z]{2,4}'


result = re.search(regex, string)

if result:
    print("OK")
else:
    print("WRONG")

#info@maktabkhooneh.org
#OK
