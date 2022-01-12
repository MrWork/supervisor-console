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

    [program:web]
    command = ...
    stdout_events_enabled = true
    stderr_events_enabled = true

    [eventlistener:stdout]
    command = /usr/bin/env python3 -m supervisor_console
    buffer_size = 100
    events = PROCESS_LOG
    result_handler = supervisor_console.events:event_handler

To use a custom log format, add `--format` to the command:

    command = /usr/bin/env python3 -m supervisor_console --format '-> {line}'

Supported placeholders are:

- `{processname}`
- `{timestamp}`
- `{line}`
