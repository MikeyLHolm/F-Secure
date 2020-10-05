#!/usr/bin/python3
import os, requests, sys
from datetime import datetime

class ResponseInfo(object):
    def __init__(self, date_time, web_site, response_status_code, response_time):
        self.date_time = date_time
        self.web_site = web_site
        self.status_code = str(response_status_code)
        self.response_time = str(response_time)

blue = '\033[94m'
endc = '\033[0m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'

def get_response_object(date_time_str, response, web_site):
    response_status_code = response.status_code
    response_time = response.elapsed.total_seconds()
    response_object = ResponseInfo(date_time_str, web_site, response_status_code, response_time)
    return response_object

def log_response(response_log, response_object):
    response_log.write(response_object.date_time + '\n')
    response_log.write(response_object.web_site + '\n')
    response_log.write("Status code: " + response_object.status_code + '\n')
    response_log.write("Response time: " + response_object.response_time + "\n\n")

# REMEMBER HTTP!
def run_requests():
    web_sites = [
        'https://www.f-secure.com/fi',
        'https://www.hive.fi/en/',
        'https://www.python.org',
        'http://www.foobar.com/login'
    ]
    if not os.path.isdir("logs/"):
        print(yellow + 'Creating logs/' + endc)
        os.mkdir("logs")

    file_name = os.path.join("logs/", "monitor_log")
    try:
        response_log = open(file_name, "a")
    except OSError:
        print (red + "Could not open/read file:" + file_name + endc)
        sys.exit()

    print(yellow + 'Running requests' + endc)
    for web_site in web_sites:
        date_time_str = str(datetime.now())
        response = requests.get(web_site)
        response_object = get_response_object(date_time_str, response, web_site)
        log_response(response_log, response_object)

    response_log.close



def main():
    # add intervals
    run_requests()
    print(green + 'Requests done. Logs are located at logs/monitor_log' + endc)

if __name__ == '__main__':
    main()