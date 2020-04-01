#Open Source webpage creator

wrt = open('index.html','w')

print("First, give your website a title")
title = input("Title:")


first = "<html> <head>"
title1 = "<title>"
title2 = "</title>"
body = "</head> <body>"
script = ""
style = ""

nnc = input("Do you want to add a logo?(y/n)")

if nnc == "y":
 nnc2 = input("URL/path:")
 width = input("Width:")
 height = input("Height:")
 align = input("Align(center/right/left):")


img = "<img src=\""+nnc2+"\" width=\""+width+"\" height=\""+height+"\" align=\""+align+"\""


scndchoice = input("The default background is in white color.Do you want to change color(1)?If not, press any other char")

if scndchoice == "1":
 color = input("Color:")
 style = "<style> body {background-color:"+color+";} </style>"


step1 = first+title1+title+title2+body+style+img
wrt.write(step1)

fontsize = input("Type size of a font(1 is the biggest,6-the smallest)")

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
