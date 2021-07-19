#! /usr/local/bin/python3

#print("content-type:text/html; charset=UTF-8\n")
#print()

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()


#Redirection
print("Location: index.py?id="+title)
print()

