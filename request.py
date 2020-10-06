import os, requests, sys
from config_files import config
from datetime import datetime
from response import get_response_object, log_response

blue = '\033[94m'
endc = '\033[0m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'


def get_requirement():
    if config['check']['requirement'] is not '':
        return config['check']['requirement']
    else:
        return None

def filter_requirement(requirement, web_site):
    if web_site.endswith('/'):
        web_site = web_site[:-1]
    address_end = web_site[web_site.rfind('/') + 1:]
    if requirement in address_end:
        return 1
    else:
        return 0

def send_requests():
    web_sites = open('site_list.txt').read().splitlines()
    requirement = get_requirement()

    if not os.path.isdir("logs/"):
        print(yellow + 'Creating logs/' + endc)
        os.mkdir("logs")

    file_name = os.path.join("logs/", "monitor_log")
    try:
        response_log = open(file_name, "a")
    except OSError:
        sys.exit(red + "Could not open/read file:" + file_name + endc)

    print(yellow + 'Running requests: ' + str(datetime.now()) + endc)

    for web_site in web_sites:
        date_time_str = str(datetime.now())
        response = requests.get(web_site)
        response_object = get_response_object(date_time_str, response, web_site)
        if requirement:
            if not filter_requirement(requirement, response_object.web_site):
                continue
        log_response(response_log, response_object)

    response_log.close
