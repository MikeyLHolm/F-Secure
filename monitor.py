#!/usr/bin/python3
import os, requests
from datetime import datetime

class ResponseInfo(object):
    def __init__(self, date_time, site, response_status_code, response_time):
        self.date_time = date_time
        self.web_site = site
        self.status_code = response_status_code
        self.response_time = response_time

blue = '\033[94m'
endc = '\033[0m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'


def log_response(date_time_str, response, response_log, site):
    response_status_code = response.status_code
    response_time = response.elapsed.total_seconds()

    response_log.write(date_time_str)
    response_log.write("\n" + site )
    response_log.write("\nStatus code: " + str(response_status_code))
    response_log.write("\nResponse time: " + str(response_time) + "\n\n")

    response_object = ResponseInfo(date_time_str, site, response_status_code, response_time)
    response_object
    print(response_object.date_time)

# REMEMBER HTTP!
def run_requests():
    print('inside requests')
    web_sites = [
        'https://www.f-secure.com/fi',
        'https://www.hive.fi/en/',
        'https://www.python.org',
        'http://www.foobar.com/login'
    ]

    response_log = open(os.path.join("logs/", "monitor_log"), "a")
    for site in web_sites:
        response = requests.get(site)
        date_time_str = str(datetime.now())
        log_response(date_time_str, response, response_log, site)

    response_log.close



def main():
    print(yellow + 'Running requests' + endc)
    run_requests()
    print(green + 'Requests done. Logs are located at logs/monitor_log' + endc)

if __name__ == '__main__':
    main()