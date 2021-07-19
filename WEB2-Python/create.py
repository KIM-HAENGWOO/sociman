#! /usr/local/bin/python3

print("content-type:text/html; charset=UTF-8\n")
print()
import cgi, os, view

form = cgi.FieldStorage()

if "id" in form:
      pageId = form["id"].value
      description = open('data/'+pageId, 'r').read()
else:
      pageId = 'HELLO'
      description = open(pageId, 'r').read()

print('''<!doctype html>
      <html>
        <head>
        <title>WEB1 - Welcome</title>
        <meta charset="utf-8">
        </head>
        
        <body>
        <h1><a href="index.py">WWW</a></h1>
        <ol>
            {listStr}
        </ol>
        <form action="process_create.py" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea rows="10" name="description" placeholder="description"></textarea></p>
            <p><input type="submit"></p>
        </form>
        </body>
      </html>'''.format(title=pageId, 
                        desc=description, 
                        listStr=view.getList()))
                        
