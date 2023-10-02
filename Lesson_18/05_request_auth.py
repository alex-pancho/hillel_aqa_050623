import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import base64

# basic = HTTPBasicAuth('user', 'pass')
#
# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
# print(r.status_code)
# print(r.request.headers)
# convertbytes = r.request.headers['Authorization'].split('Basic ')[-1].encode("ascii")
# convertedbytes = base64.b64decode(convertbytes)
# print(convertedbytes)


# https://en.wikipedia.org/wiki/Digest_access_authentication
url = 'https://httpbin.org/digest-auth/auth/user/pass'
r = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
#r = requests.get(url, auth=None)
print(r.status_code)
print(r.text)
print(r.request.headers)