# from authlib.jose import jwt
# header = {'alg': 'RS256'}
# payload = {'iss': 'Authlib', 'sub': '123', ...}
# key = read_file('private.pem')
# s = jwt.encode(header, payload, key)

from authlib.jose import jwt

with open('private.pem', 'rb') as f:
    key = f.read()
