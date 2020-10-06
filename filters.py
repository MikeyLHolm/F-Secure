from config import config

def check_content_requirement(content_requirement, text):
    if content_requirement in text:
        return True
    else:
        return False

def get_content_requirement():
    if config['check']['content_requirement'] is not '':
        return config['check']['content_requirement']
    else:
        return None

def get_filter_str():
    if config['check']['filter_str'] is not '':
        return config['check']['filter_str']
    else:
        return None

def filter_url(filter_str, url):
    if url.endswith('/'):
        url = url[:-1]
    address_end = url[url.rfind('/') + 1:]
    if filter_str in address_end:
        return True
    else:
        return False

def use_filters(response_object):
    filter_str = get_filter_str()
    content_requirement = get_content_requirement()
    if filter_str and not content_requirement:
        if not filter_url(filter_str, response_object.url):
            return 0
        else:
            return 1
    elif content_requirement:
        if not check_content_requirement(content_requirement, response_object.txt):
            return 0
        else:
            return 1
    return 1
