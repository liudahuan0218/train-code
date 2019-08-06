from urllib.request import urlopen

response = urlopen("http://www.baidu.com")
print(type(response))
html = response.read()
print(html)
