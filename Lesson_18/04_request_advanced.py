import requests


# s = requests.Session()
#
# s.get('https://httpbin.org/cookies/set/sessioncookie/1234')
# r = s.get('https://httpbin.org/cookies')
#
# print(r.text)  # '{"cookies": {"sessioncookie": "1234"}}'



# session pool
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=10,
    pool_maxsize=100)
session.mount('http://', adapter)
response = session.get("http://example.org")
print(response.status_code)
print(response.text)


# url = 'https://httpbin.org/post'
#
# multiple_files = [
#     ('images', ('small.png', open('small.png', 'rb'), 'image/png')),
#     ('images', ('crab.png', open('crab.png', 'rb'), 'image/png'))]
#
# r = requests.post(url, files=multiple_files)
# print(r.text)
#

# download large files
def download_file(target_url, local_filename=None):
    if local_filename is None:
        local_filename = target_url.split('/')[-1]
    with requests.get(target_url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


download_file('https://e7.pngegg.com/pngimages/778/849/png-clipart-computer-icons-user-login-avatar-small-icons-angle-heroes.png',
              local_filename='man.png')
#download_file('https://e7.pngegg.com/pngimages/778/849/png-clipart-computer-icons-user-login-avatar-small-icons-angle-heroes.png')
