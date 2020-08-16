from supervisor.events import Event
from supervisor.options import ServerOptions
from sys import stderr, stdout
from typing import Dict, BinaryIO
from datetime import datetime

__log_format="{processname} | {timestamp::%Y-%m-%d %H:%M:%S} | {time}"

#def __set_log_format(value: str) -> None:
#    if value:
#        __log_format = value

__CHANNEL_MAP : Dict[str, BinaryIO] = dict(stdout = stdout, stderr = stderr)
#__options = ServerOptions()
#__options.add('logformat', 'supervisorconsole.logformat', handler=__set_log_format, default=__log_format, env="SUPERVISOR_CONSOLE_LOGFMT")
#__options.realize()

def event_handler(event : Event, response : str) -> None:
    header_line, data = response.split('\n', 1)
    headers = dict([ x.split(':') for x in header_line.split() ])
    lines = data.split('\n')
    processname, channel_name = headers['processname'], headers['channel']
    
    channel = __CHANNEL_MAP[channel_name] if channel_name in __CHANNEL_MAP.keys() else stdout

    timestamp: datetime = datetime.utcnow()
    text = '\n'.join( __log_format.format(processname=processname, timestamp=timestamp, line=line) for line in lines)

    print(text, file = channel)
