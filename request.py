import os, requests, sys
from config import config, blue, endc, green, red, yellow
from datetime import datetime
from response import get_response_object
from log_write import log_response, log_timeout, log_too_many_redirects
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def get_requirement():
    if config['check']['requirement'] is not '':
        return config['check']['requirement']
    else:
        return None

def filter_requirement(requirement, url):
    if url.endswith('/'):
        url = url[:-1]
    address_end = url[url.rfind('/') + 1:]
    if requirement in address_end:
        return 1
    else:
        return 0

def request_loop(requirement, response_log,  url):
    print(blue + 'Sending request to ' + url + endc)
    date_time_str = str(datetime.now())
    try:
        response = requests.get(url, allow_redirects=3, verify=False, timeout=5)
    except requests.exceptions.Timeout:
        log_timeout(date_time_str, response_log, url)
        return
    except requests.exceptions.TooManyRedirects:
        log_too_many_redirects(date_time_str, response_log, url)
        return
    except requests.exceptions.RequestException as e:
        print(red + 'Sheeeet, Major Issues reporting to duty' + endc)
        raise SystemExit(e)
    if response.status_code is not 200:
        print(red + 'Anomaly in status codes:', response.status_code, response.reason + endc)
    response_object = get_response_object(date_time_str, response, url)
    if requirement:
        if not filter_requirement(requirement, response_object.url):
            return
    log_response(response_log, response_object)

def send_requests():
    if not os.path.isdir('logs/'):
        print(yellow + 'Creating logs/' + endc)
        os.mkdir('logs')
    file_name = 'site_list.txt'
    try:
        web_sites = open(file_name).read().splitlines()
        file_name = os.path.join('logs/', 'monitor_log')
        response_log = open(file_name, 'a')
    except OSError:
        raise SystemExit(red + 'Could not open/read file: ' + file_name + endc)
    requirement = get_requirement()
    print(yellow + 'Sending requests: ' + str(datetime.now()) + endc)
    for url in web_sites:
        request_loop(requirement, response_log, url)
    response_log.close
