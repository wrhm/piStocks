import re

f = open('bizyahoo.txt','r')
text = f.read()
f.close()

#pattern = '>.{1,5}</a></td><td\W{5,15}[\d\.]+'
pattern = '>([A-Z\.]{1,5})</a></td><td[^>]*>([\d\.]+)'
print re.findall(pattern,text)

