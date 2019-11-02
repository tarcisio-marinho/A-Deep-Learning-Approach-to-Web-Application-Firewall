#!/usr/bin/python3.6
import sys
import os
import random
import subprocess

def is_valid_file(path):
    if(not os.path.isfile(path)):
        return False
    return True

def delete_input_file(path):
    os.remove(path)

def identify(model_path, payload):
    command = "fasttext predict %s %s" %(model_path, payload)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout = process.stdout.readlines()
    stderr = process.stderr.readlines()
    
    if(stderr):
        print(stderr)
    else:
        label = [payload.replace("__label__", "").replace("\n", "") for payload in stdout]
        print(label)
            
if __name__ == "__main__":
    model = 'models/model2.bin'
    if(len(sys.argv)< 2):
        print('invalid sintaxe, input file missing?')
        sys.exit()
        
    payload = sys.argv[1]
    if(is_valid_file(payload)):
        identify(model, payload)

    else:
        print("invalid input file")
