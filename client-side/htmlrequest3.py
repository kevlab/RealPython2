import requests

url = 'http//httpbin.org/post'
data = {'fname': 'somename', 'lname': 'somelastname'}

r = requests.post(url, data=data)

print r
print "___CONTENT__"
print r.content
