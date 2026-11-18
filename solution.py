import base64

def solve(value):
    return base64.b64decode(value, validate=True).decode('utf-8')
