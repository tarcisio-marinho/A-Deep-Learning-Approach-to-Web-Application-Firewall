import os
import sys
import json
import traceback
import logging

def warn(msg, exception):
    sys.stderr.write('\033[91mERROR: \033[0m' + msg + '\n')

    for line in traceback.format_exception(None, exception, exception.__traceback__):
        print(line, file=sys.stderr, flush=True)


def error(msg, exception, status_code):
    sys.stderr.write('\033[91mERROR: \033[0m' + msg + '\n')

    for line in traceback.format_exception(None, exception, exception.__traceback__):
        print(line, file=sys.stderr, flush=True)

    sys.stderr.write('Exiting producer...\n')
    sys.exit(status_code)

