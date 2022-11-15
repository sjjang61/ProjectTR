import urllib

def requestUrl( url, headers = {}):
    req = urllib.request.Request(url, headers=headers )
    response = urllib.request.urlopen(req).read()
    try:
        content = response.decode('utf-8')
    except UnicodeDecodeError:
        content = response

    print("[RES] content = %s " % (content))
    return content