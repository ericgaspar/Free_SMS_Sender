#! /usr/bin/python

import requests

# msg : votre message
msg = list("message")
# user : votre identifiant freemobile, du type 11111111
user = "user"
# pass : votre clé d’identification freemobile
password = "password"

encodingTable={"\n":"%0A"," ":"%20","!":"%21","\"":"%22","#":"%23",
		"$":"%24","%":"%25","&":"%26","'":"%27","(":"%28",
		")":"%29","*":"%2A","+":"%2B",",":"%2C","-":"%2D",
		".":"%2E","/":"%2F",":":"%3A",";":"%3B","<":"%3C",
		"=":"%3D",">":"%3E","?":"%3F"}

def sendMessage(msg,user=user,password=password):
	for char in msg:
		if char in encodingTable:
    		char=encodingTable[char]
	msg="".join(msg)

	url="https://smsapi.free-mobile.fr/sendmsg?user="+user+"&pass="+password+"&msg="+msg
	requests.get(url)
