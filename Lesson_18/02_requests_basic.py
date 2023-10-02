# https://en.wikipedia.org/wiki/HTTP
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# https://requests.readthedocs.io/en/latest/api/#status-code-lookup
# https://requests.readthedocs.io/en/latest/
import requests

# get
# response = requests.get('https://randomuser.me/api/')
# #response = requests.get('https://google.com')
# print(dir(response))
# print(response.status_code)
# print(response.reason)
# print(response.url)
# # print(response.text)
# ####################################
# result = response.json()
# print(type(result))


# # raw response content
# r = requests.get('https://api.github.com/events', stream=True)
# # print(r.text)
# # #print(r.json())
# # print(r.raw)
# # print(r.raw.read(10))
# with open('response.txt', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)
#     print('-'*30)

# post
r = requests.post('https://httpbin.org/post', data={'key1': 'value1'})
print(r.status_code)
print(r.json())

# url = 'https://api.github.com/some/endpoint'
#
# headers = {'User-Agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)
# print(r.request.headers)
# print(r.headers)


# # response codes
# bad_r = requests.get('https://httpbin.org/status/404')
# #bad_r = requests.get('https://google.com')
#
# print(bad_r.status_code)
#
# bad_r.raise_for_status()

# timeouts
#r = requests.get('https://github.com', timeout=0.001)
# r = requests.get('https://github.com', timeout=5)

# cookies
url = 'http://example.com/some/cookie/setting/url'

r = requests.get(url)

print(r.cookies.values())


