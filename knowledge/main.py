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

def identify(fasttext_path, model_path, payload):
    command = "./%s predict %s %s" %(fasttext_path, model_path, payload)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout = process.stdout.readlines()
    stderr = process.stderr.readlines()
    
    if(stderr):
        print(json.dumps(stderr))
    else:
        label = [output.decode('utf-8').replace("__label__", "").replace("\n", "") for output in stdout]
        print(json.dumps(label))
        
    delete_input_file(payload)
            
if __name__ == "__main__":
    if(len(sys.argv)< 4):
        print('invalid sintaxe, model or input file missing?')
        sys.exit()
    
    
    model = sys.argv[1]
    payload = sys.argv[2]
    fasttext_path = sys.argv[3]
    
    if(is_valid_file(payload) and is_valid_file(model)):
        identify(fasttext_path, model, payload)

    else:
        print("invalid input file")
