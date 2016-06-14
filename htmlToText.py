import html2text

html = open("wiki.html").read()
print html2text.html2text(html)
