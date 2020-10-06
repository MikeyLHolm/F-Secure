#!/usr/bin/python3
import schedule, time
from config_files import config
from request import send_requests

blue = '\033[94m'
endc = '\033[0m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'

def main():

    checking_period = int(config['check']['checking_period'])

    if checking_period > 0:
        schedule.every(checking_period).seconds.do(send_requests)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        send_requests()
    print(green + 'Requests done. Logs are located at logs/monitor_log' + endc)

if __name__ == '__main__':
    main()