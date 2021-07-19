#! /usr/local/bin/python3

print("content-type:text/html; charset=UTF-8\n")
print()
# 첫번째 프린트문은 헤더정보를 담고 있는데 헤더정보 다음에 반드시 줄바꿈이 있어야 하기 때문.한줄로 줄이고 싶다면 첫 번째 프린트문 뒤에 \n을 붙이시면 됩니다.
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()

if "id" in form:
      title = pageId = form["id"].value
      title = sanitizer.sanitize(title)
      description = open('data/'+pageId, 'r').read()
      #description = sanitizer.sanitize(description) : 이미지 파일 표시가 sanitizer 되어버림
      update_link = '<a href="update.py?id={}">UPDATE</a>'.format(pageId)
      delete_action = '''
            <form action="process_delete.py" method="post">
                  <input type="hidden" name="pageId" value="{}">
                  <input type="submit" value="delete">
            </form>
      '''.format(pageId)
else:
      title = pageId = 'HELLO'
      description = open(pageId, 'r').read()
      update_link = ''
      delete_action = ''

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
        <a href="create.py">CREATE</a>
        {update_link} 
        {delete_action}
        <h2>{title}</h2>
        <p>{desc}</p>
        </body>
      </html>'''.format(title=title, 
                        desc=description, 
                        listStr=view.getList(), 
                        update_link=update_link, 
                        delete_action=delete_action))
