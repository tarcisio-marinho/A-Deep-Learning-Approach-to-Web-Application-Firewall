#!/usr/bin/python3.6
import sys
import os
import random

def is_valid_file(path):
    if(not os.path.isfile(path)):
        return False
    return True

def identify(payload):
    return random.choice(['xss', 'sqli', 'path-traversal', 'valido', 'rce', 'xxe'])
        
if __name__ == "__main__":
    if(len(sys.argv)< 2):
        print('invalid sintaxe')
        sys.exit()
        
    if(is_valid_file(sys.argv[1])):
        with open(sys.argv[1], 'rb') as f:
            payload = f.read()
        print(identify(payload))
        
    else:
        print("invalid input")
