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
        print('python create_model.py dataset_path new_model_path fasttext_path\n')
        print("[dataset_path] has to be a valid dataset to train")
        print("[new_model_path] filename to the new model that will be trained")
        print("[fasttext_path] is the path to the fasttext binary. this project contains on disk the binary")
        sys.exit(1)
        
    elif(file == 'dataset'):
        print('usage: ')
        print('python create_dataset.py dataset_name\n')
        print('[dataset_name] is the name of the new dataset that will be created')
        sys.exit(1)
