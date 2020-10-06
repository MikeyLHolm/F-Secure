
Storing response in object?

	I felt its easier to manipulate the response date later when its already in an object.
	Usage of data may change in the future -> keeping options open.

Opening and closing of file?

Dependant of the use of software. For ex a SW that runs every 24h it would be silly
to keep file open for 23h55mins after finishing with the requests in 5mins. So I chose to open
and close the log at the start and end of request loop.

Config.ini?
	if checking_period > 0 loop requests for with interval of checking_period
	else run requests once.

	if requirement is empty run requests with no filters.
	else filter final part of web site addresses with requirement:

		e.g. requirement = login then everything including last '/' is removed and
		then comparison requirement.in(remainder_of_str) is done.

			One exception remains: if '/' is last char of string it is being removed before the previous section.

Status Codes: 301,302,303, 307, 308
	Allowing following error msg:
		InsecureRequestWarning: Unverified HTTPS request is being made to host 'httpstat.us'.
		Adding certificate verification is strongly advised.
		See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  		InsecureRequestWarning,


:: UPGRADES ::

Intervals?
	Don't take into account running time of the request function.

Log time?
	Could have GMT added.

Running requests: 2020-10-05 17:54:18.946163?
	To be same as first request.

Run program in Crontab?

Separate log for not 200 status codes?

Flag to manipulate Interval time?

Output to different type of log file (.csv/json)?