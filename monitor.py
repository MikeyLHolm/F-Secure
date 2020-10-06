#!/usr/bin/python3
import schedule, time
from config import config,blue,endc,green,red,yellow
from request import send_requests

def main():
    checking_period = int(config['init']['checking_period'])
    try:
        if checking_period > 0:
            schedule.every(checking_period).seconds.do(send_requests)
            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            send_requests()
    except KeyboardInterrupt:
        print(' KeyboardInterrupt handled')
    print(green + 'Requests done. Logs are located at logs/monitor_log' + endc)

if __name__ == '__main__':
    main()