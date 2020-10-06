class ResponseInfo(object):
    def __init__(self, date_time, url, response_status_code, response_status_msg, response_time):
        self.date_time = date_time
        self.url = url
        self.status_code = response_status_code
        self.status_msg = response_status_msg
        self.response_time = response_time

def get_response_object(date_time_str, response, url):
    response_status_code = response.status_code
    response_status_msg = response.reason
    response_time = response.elapsed.total_seconds()
    response_object = ResponseInfo(date_time_str, url, response_status_code,
                                   response_status_msg, response_time)
    return response_object
