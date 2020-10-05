#!/usr/bin/python3
import os, requests
from datetime import datetime

def log_response(date_time_str, response, site):
    response_status_code = response.status_code
    response_time = response.elapsed.total_seconds()
    # print(response_status_code)
    # print(response_time)

    # better to open and close outside and use this to just write??
    response_log = open(os.path.join("logs/", "monitor_log"), "a")
    response_log.write("\n______________________________________\n")
    response_log.write(date_time_str)
    response_log.write("\n\t" + site )
    response_log.write("\n\tStatus code: " + str(response_status_code))
    response_log.write("\n\tResponse time: " + str(response_time))
    response_log.write("\n______________________________________\n")
    response_log.close

# REMEMBER HTTP!
def run_requests():
    print('inside requests')
    web_sites = [
        'https://www.f-secure.com/fi',
        'https://www.hive.fi/en/',
        'https://www.python.org',
        'http://www.foobar.com/login'
    ]
    for site in web_sites:
        #print(site)
        response = requests.get(site)
        date_time_str = str(datetime.now())
        log_response(date_time_str, response, site)
    #print(web_sites)
    # r = requests.get('https://www.python.org')
    # r_status_code = r.status_code
    # r_response_time = r.elapsed.total_seconds()
    # print(r_status_code)
    # print(r_response_time)
    # r = requests.get('http://www.foobar.com/login')
    # print(r.status_code)
    # print(r.elapsed.total_seconds())



def main():
    print('Running list of websites')
    run_requests()


if __name__ == '__main__':
    main()