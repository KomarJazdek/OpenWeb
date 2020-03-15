#/usr/bin/python3
#pre-alpha version of Open Web
#This is a software for making websites without web technologies knowledge

wrt = open('index.html','w')

print("First, give your website a title")
title = input("Title:")


first = "<html> <head>"
title1 = "<title>"
title2 = "</title>"
body = "</head> <body>"


step1 = first+title1+title+title2+body
wrt.write(step1)
count = 0
while count < 10:
 textinp = input("Line of the text:")
 textinp += "<br>"
 count += 1
 wrt.write(textinp)


step2 = "</body> </html>"
wrt.write(step2)
wrt.close()

