# F-Secure
Assignment for F-Secure Security Cloud team -application. Assignment can be found after my solution.

## My solution

My goal was to make monitor easy to read, flexible and modular. Small functions without many purposes for each. I chose Python due it being the most familiar language for me after C plus the insane versatility and simplicity. And it was done in virtual env so you don't have to install all the unnecessary packages and can instead just install required ones from txt file. 
I'm not familiar with the various logging options in Python so I decided to do it by writing simple file with the necessary information. It will log every response but only non-200 reponses are written in terminal as anomalies.

I decided to store needed response data in a object. I felt its easier to manipulate the data later if the needs change when its already in an object.
And its lots cleaner as well.

Setuping program can be done at config.ini.

```
if checking_period > 0 
	loop requests for with interval of checking_period
else 
	run requests once. Initial value is 0.
  
content_requirement and filter_str work as one. Values should be given without '  or  ".
e.g. content_requirement = login

if content_requirement 
	it is always used as filterer and searches response.text for match.
elif filter_str
	use filter_str as filterer for final part of web site addresses with requirement:
	e.g. filter_str = login
	then everything including last '/' is removed ('http://www.foobar.com/login' would leave 'login')
	then comparison filter_str.in(remainder_of_url) is done.

	One exception remains: if '/' is last char of string it is being removed before the previous section.
else
	as both fields are empty, run requests with no filters.
```

Few raised questions that remain:

* Redirecting requests return 200 instead original redirect status code if redirect is OK. Would it be better to have the initial status code instead?
* Opening and closing the log file? I chose to open and close the log at the start and end of request loop. If it runs continuouslyit would be better choice to keep the file open for whole duration I suppose.
* Optimal way of testing this kind of program? Unit tests work fine for something like an object but should responses be tested with mock?

### How to use
Clone the repo:

```git clone https://github.com/MikeyLHolm/F-Secure.git```

Install necessary packages from requirement.txt:

```pip3 install -r requirements.txt```

Setup config file:

```
[init]
# When checking_period = 0 requests are sent only once. With values n > 0 software runs ~every n seconds unless runtime > n.

checking_period = 0

# 'content_requirement = login' would search response.text string for match to login for every request and only logging sites with found match.
# Same for filter_str except it works only if content_req is empty. Filter_str searches matches from last part of url.

content_requirement =
filter_str =
```

Run activity monitor:

```python3 monitor.py```

Run unit tests for ReponseObject:

```python3 test_object.py```

Choosing different test file:

```
Edit row 34 in request.py
file_name = 'site_list.txt'
to match your file name in root of project.
```

### Possible Improvements
* Intervals don't take into account running time of the request function. If running time of function if longer than checking_period it runs 1s after finishing with the ongoing function.
* Log time could have GMT + 3 added if software is used in various timezones.
* Initial running time isn't same as time when first response is sent.
* Run program in Crontab.
* Separate log for not 200 status codes? Perhaps -flag operated?
* Ability to manipulate checking_period/content_requirement with flags from command line.
* Output to different type of log file (.csv/json).

# Original Task

## Coding Task Description

Implement a program that monitors web sites and reports their availability. This tool is intended as a monitoring tool for web site administrators for detecting problems on their sites.

### Main functions:

1.	Reads a list of web pages (HTTP URLs) and corresponding page content requirements from external configuration.
2.	Periodically makes an HTTP request to each page.
3.	Verifies that the page content received from the server matches the requirements in the configuration.
4.	Measures the time it took for the web server to complete the whole request.
5.	Writes a log that contains the progress of the periodic checks.

### Details:

•	The “content requirement” can for example be just a simple string that must be included in the response received from the server, e.g. one rule might be that the page at the URL “http://www.foobar.com/login” must contain the text “Please login:”.
•	The checking period must be configurable via a command-line option or by a setting in the configuration file.
•	The log file must contain the checked URLs, their status and the response times.
•	The program must distinguish between connection level problems (e.g. the web site is down) and content problems (e.g. the content requirements were not fulfilled).

There is a lot of freedom to choose software technologies, tools and file formats to achieve the goal.

Note that the task is meant for evaluating both software development and software architecture design skills. Pay attention to the design of applications you create.

It is necessary to personally write the source code, but it does not have to be complete.

### Deliverables:

The software is delivered with the full source code included. All used source code must be freely distributable.

If necessary, include readme.txt to describe the software and how it meets the requirements.


## Optional: Design question

Assuming we wanted to simultaneously monitor the connectivity (and latencies) from multiple geographically distributed locations and collect all the data to a single report that always reflects the current status across all locations. Describe how the design would be different. How would you transfer the data? Security considerations?
