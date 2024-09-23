<h1>Python Log Parser</h1>

<h2>Summary</h2>
<p>
  This script parses two log files, Log-A.strace and Log-B.strace, to identify and count different types of read() system call events. It distinguishes between general read events, keyboard reads (detected by the presence of tty), and file reads (excluding keyboard and pipe-related events). Additionally, it extracts and displays filenames associated with file read events. In the end, the script summarizes the total counts for each type of event, providing a breakdown of read operations from both logs.
</p>
