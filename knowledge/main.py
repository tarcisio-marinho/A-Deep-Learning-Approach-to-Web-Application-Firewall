#!/usr/bin/python3.6
import sys
import os
import random
import subprocess
import json

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
        print(json.dumps(stderr))
    else:
        label = [payload.replace("__label__", "").replace("\n", "") for payload in stdout]
        print(json.dumps(label))
            
if __name__ == "__main__":
    if(len(sys.argv)< 3):
        print('invalid sintaxe, model or input file missing?')
        sys.exit()
        
    model = sys.argv[1]
    payload = sys.argv[2]
    
    if(is_valid_file(payload) and is_valid_file(model)):
        identify(model, payload)

    else:
        print("invalid input file")
