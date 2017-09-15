import requests
r = requests.get('http://bbs.8080.net')
print type(r)
print r.status_code
print r.encoding