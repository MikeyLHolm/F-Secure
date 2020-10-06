blue = '\033[94m'
endc = '\033[0m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'

class ResponseInfo(object):
    def __init__(self, date_time, web_site, response_status_code, response_time):
        self.date_time = date_time
        self.web_site = web_site
        self.status_code = str(response_status_code)
        self.response_time = str(response_time)

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
