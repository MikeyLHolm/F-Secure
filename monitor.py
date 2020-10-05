#!/usr/bin/python3
import os, requests, sys
import schedule, time
from datetime import datetime
from config_files import config

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

# if after last / containt login return 1
def parse_requirement(requirement, web_site):
    if web_site.endswith('/'):
        web_site = web_site[:-1]
    address_end = web_site[web_site.rfind('/') + 1:]
    if requirement in address_end:
        return 1
    else:
        return 0

# REMEMBER HTTP!
def run_requests():
    web_sites = [
        'https://www.f-secure.com/fi',
        'https://www.hive.fi/en/',
        'https://www.python.org',
        'http://www.foobar.com/login'
    ]

    if config['check']['requirement'] is not '':
        requirement = config['check']['requirement']
    else:
        requirement = None

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
            if not parse_requirement(requirement, response_object.web_site):
                continue
        log_response(response_log, response_object)

    response_log.close



def main():

    checking_period = int(config['check']['checking_period'])

    if checking_period > 0:
        schedule.every(checking_period).seconds.do(run_requests)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        run_requests()
    print(green + 'Requests done. Logs are located at logs/monitor_log' + endc)

if __name__ == '__main__':
    main()