#!/usr/bin/python3.6
import sys
import os
import random
import subprocess
import json
from utils import *

def is_valid_file(path):
    if(os.path.isfile(path)):
        return False
    return True


def identify(fasttext_path, train_dataset, model_output):
    command = "./%s supervised -input %s -output %s" %(fasttext_path, train_dataset, model_output)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stderr = process.stderr.readlines()
    
    for i in stderr:
        print(i.decode())
    print('model created !')
    print('model path:', model_output + '.bin')
        
            
if __name__ == "__main__":
    if(len(sys.argv)< 2):
        print_help('model')
        
    output = sys.argv[1]
    if(output == "--h" or output == '--help' or output == "-h"):
        print_help('model')
    
    if(len(sys.argv)< 4):
        print('invalid sintaxe, model or input file missing?')
        sys.exit()
    
    train_dataset = output
    modelname = sys.argv[2]
    fasttext_path = sys.argv[3]
    
    if(os.path.isfile(fasttext_path) and is_valid_file(modelname) and os.path.isfile(train_dataset)):
        identify(fasttext_path, train_dataset, modelname )

    else:
        print_help("model")
