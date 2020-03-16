#Pre-alpha of Open Web
#Open Source webpage creator

wrt = open('index.html','w')

print("First, give your website a title")
title = input("Title:")


first = "<html> <head>"
title1 = "<title>"
title2 = "</title>"
body = "</head> <body>"


step1 = first+title1+title+title2+body
wrt.write(step1)

fontsize = input("Type size of a font(1 is the biggest)")

try:
 while True:
  textinp = input("Line of the text:")
  font = "<h" + fontsize + ">"
  text = font + textinp
  text += "</h"+fontsize+">"
  wrt.write(text)
except:
 font = "<h" + fontsize + ">"
 text = font + textinp
 text += "</h"+fontsize+">"
 text += "<br>"
 wrt.write(text)
 
 
step2 = "</body> </html>"
wrt.write(step2)
wrt.close()
