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

def print_help(file):
    if(file == 'model'):
        print('usage: ')
        print('python create_model.py dataset_path new_model_path fasttext_path')
        sys.exit(1)
        
    elif(file == 'dataset'):
        print('usage: ')
        print('python create_dataset.py dataset_name')
        sys.exit(1)
