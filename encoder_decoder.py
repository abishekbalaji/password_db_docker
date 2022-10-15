import base64

def encoder(text):
    return base64.b64encode(bytes(text, 'UTF-8')).decode('UTF-8')

def decoder(text):
    return base64.b64decode(bytes(text, 'UTF-8')).decode('UTF-8')
