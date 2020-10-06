Storing response in object?

	I felt its easier to manipulate the response date later when its already in an object.
	Usage of data may change in the future -> keeping options open.

Opening and closing of file?

    I chose to open and close the log at the start and end of request loop. If it runs continuously
    it would be better choice to keep the file open for whole duration.

Config.ini?
	if checking_period > 0 loop requests for with interval of checking_period
	else run requests once.

    content_requirement and filter_str work as one. Values should be given without '  or  ".
    e.g. content_requirement = login

    if content_requirement is present it is always used as filterer and searches response.text for match.

	else filter final part of web site addresses with requirement:

		e.g. requirement = login then everything including last '/' is removed and
		then comparison requirement.in(remainder_of_str) is done.

			One exception remains: if '/' is last char of string it is being removed before the previous section.

    if both fields are empty, run requests with no filters.


Redirecting requests return 200 instead original redirect status code if redirect is OK.

Setuping virtual env from requirement.txt?
    pip3 install -r requirements.txt

:: UPGRADES ::

Intervals?
	Don't take into account running time of the request function.

Log time?
	Could have GMT added.

Running requests: 2020-10-05 17:54:18.946163?
	To be same as first request.

Run program in Crontab?

Separate log for not 200 status codes?
    -flag operated?

Flag to manipulate Interval time?

Output to different type of log file (.csv/json)?

:: BUGS ::