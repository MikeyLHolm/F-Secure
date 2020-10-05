-
-
- Flag to manipulate Interval time
- read list from file
- output to different type of log file (.csv/json)



Storing response in object?

	I felt its easier to manipulate the response date later when its already in an object.
	Usage of data may change in the future -> keeping options open.

Opening and closing of file?

Dependant of the use of software. For ex a SW that runs every 24h it would be silly
to keep file open for 23h55mins after finishing with the requests in 5mins. So I chose to open
and close the log at the start and end of request loop.




:: UPGRADES ::

Intervals?
	Don't take into account running time of the request function.

Log time?
	Could have GMT added.