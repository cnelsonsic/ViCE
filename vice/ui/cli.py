""" Command Line Interface for ViCE

Usage:
    vice (create | edit | destroy) (plugin [-t TYPE] | database) NAME
    vice (start | stop) (client | server) [HOST -p PORT]

Commands:
    create                Create a new database or plugin.
    edit                  Edit an existing database or plugin.
    destroy               Delete an existing databse or plugin, permanently.
    start                 Start a client or server.
    stop                  Stop a running client or server.

args:
    NAME                  Name of plugin or database to be created, edited,
                          or destroyed.
    HOST                  Hostname to connect to or bind to when starting a
                          client and server, respectively [default: localhost].

Options:
    -h, --help            Show this help text and exit.
    -v, --version         Show ViCE Version.
    -t TYPE, --type TYPE  Set plugin type to TYPE [default: Item].
    -p PORT, --port PORT  The port to connect to or listen on when starting a
                          client or server, respectively [default: 8080].
"""
from docopt import docopt


def create(commands, arguments, options):
    pass

def edit(commands, arguments, options):
    pass

def destroy(commands, arguments, options):
    pass

def start(commands, arguments, options):
    pass

def stop(commands, arguments, options):
    pass

def main():
    arguments = {}
    options = {}
    commands = []
    for key, value in docopt(__doc__, version='0.0.1').items():
        if key.isupper():
            arguments[key] = value
        elif key.startswith('--') and key not in ('--help', '--version'):
            options[key] = value
        elif value:
            commands.append(key)

    if 'create' in commands:
        commands.remove('create')
        create(commands, arguments, options)
    elif 'edit' in commands:
        commands.remove('edit')
        edit(commands, arguments, options)
    if 'destroy' in commands:
        commands.remove('destroy')
        destroy(commands, arguments, options)
    elif 'start' in commands:
        commands.remove('start')
        start(commands, arguments, options)
    elif 'stop' in commands:
        commands.remove('stop')
        stop(commands, arguments, options)

if __name__ == '__main__':
    main()
