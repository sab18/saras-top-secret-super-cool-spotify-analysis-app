import base64

def import_image(file_name):
    with open( file_name,'rb') as f:
        return base64.b64encode(f.read()).decode()