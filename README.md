# supervisor-console

A simple [supervisord](http://supervisord.org/) event listener to relay
process output to supervisor's stdout and stderr.

This is useful in situations where the output will be collected and set to
external logging framework, such as Heroku, ElasticSearch (ELK), etc..

## Installation

Just install via pip or add to your requirements.txt:

    pip install supervisor-console

## Usage

An example supervisord.conf:

    [supervisord]
    nodaemon = true

    [supervisorconsole]
    logformat= ;; format of the logging. Available variables are `processname`, `timestamp` and `line` 

    [program:web]
    command = ...
    stdout_events_enabled = true
    stderr_events_enabled = true

    [eventlistener:stdout]
    command = supervisor_console
    buffer_size = 100
    events = PROCESS_LOG
    result_handler = supervisor_console:event_handler
