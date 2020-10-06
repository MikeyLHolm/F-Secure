from config import blue,endc,green,red,yellow

def log_response(response_log, response_object):
    response_log.write(response_object.date_time + '\n')
    response_log.write(response_object.url + '\n')
    response_log.write("Status code: " + str(response_object.status_code) + '\n')
    if response_object.status_msg:
        response_log.write("Status message: " + response_object.status_msg + '\n')
    response_log.write("Response time: " + str(response_object.response_time) + "\n\n")

def log_timeout(date_time_str,response_log, url):
    response_log.write(date_time_str + '\n')
    response_log.write(url + '\n')
    response_log.write('Status message: Timeout after 5s\n\n')
    print(red + 'Anomaly in request: Timeout' + endc)

def log_too_many_redirects(date_time_str,response_log, url):
    response_log.write(date_time_str + '\n')
    response_log.write(url + '\n')
    response_log.write('Status message: Timeout after 5s\n\n')
    print(red + 'Anomaly in request: Timeout' + endc)
