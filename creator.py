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

color = "white"

if nnc == "y":
 nnc2 = input("URL/path:")
 width = input("Width:")
 height = input("Height:")
 img = "<img src=\""+nnc2+"\" width=\""+width+"\" height=\""+height+"> <br>"
else:
 img = ""
indextitle = input("Title to be showed on the center of this page")

title31 = "&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    <b id=\"title\">"+indextitle+"</b> "

scndchoice = input("The default background is in white color.Do you want to change color(1)?If not, press any other char")

if scndchoice == "1":
 color = input("Color:")
 style = "<style> body {background-color:"+color+";}  </style>"

hr = "<hr style=\"color:"+color+"\>"

step1 = first+title1+title+title2+body+style+img+hr+"<br>"+title31
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
finally:
 choice_img = input("Do you want to add some photos?(y/n)")
 if choice_img == "y":
  while True:
   moreimg = input("Photo path/URL:")
   img_width = input("Width:")
   img_height = input("Height:")
   moreimg2 = "<img src=\""+moreimg+"\" width=\""+img_width
   moreimg2 += "\" height=\""+img_height+"\">"
   wrt.write(moreimg2)
  else:
   print("Ok, no photos! :)")
   
step2 = "</body> </html>"
wrt.write(step2)
wrt.close()
