
Opening and closing of file?

Dependant of the use of software. For ex a SW that runs every 24h it would be silly
to keep file open for 23h55mins after finishing with the requests. So I chose to open
and close the log at the start and end of request loop.

Intervals?

Don't take into account running time of the request function.