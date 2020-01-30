from config import config
from utils import *

import sys
import os
import random

def get_labels(path):
    if(not os.path.isdir(path)):
        error('Path: %s is invalid' %(path), IOError(), 1)
        
    return ["__label__" + label for label in os.listdir(path)]


def create_dataset(path):
    if(not os.path.isdir(path)):
        error('Path: %s is invalid' %(path), IOError(), 1)
    
    # dataset = {}
    dataset = []
    for label in os.listdir(path):
        label_name = "__label__" + label
        full_label_path = os.path.abspath(os.path.join(path, label))
        # dataset[label] = []
        for found_file in os.listdir(full_label_path):
            with open(os.path.join(full_label_path, found_file), encoding='ISO-8859-1') as f:
                contents = f.readlines()
                for content in contents:
                    if(label_name not in content):
                        dataset.append(label_name + " " + 
                                content.replace('\n', '') + '\n')
                    else:
                        dataset.append(content)

    random.shuffle(dataset)
    dataset = sorted(dataset, key=lambda x: random.random())
    return dataset

        
        
if __name__ == "__main__": 
    if(len(sys.argv)< 2):
        print_help('dataset')

    output = sys.argv[1]
    if(output == "--h" or output == '--help' or output == "-h"):
        print_help('dataset')
        
    if(os.path.isfile(output)):
        error("File:" + output + " already exists", IOError(), 5)
        
    dataset = create_dataset(config.get('dataset_path'))
    print('Dataset Created!')
    print('Dataset Size:', len(dataset))
    print('writing to disk!')
    
    try:
        if('.txt' not in output):
            output += '.txt'
        with open(output, 'w') as f:
            for i in dataset:
                f.write(i)
    except Exception as e:
        error("Error occurred", e, 20)
                    
    print("Dataset writed on file: " + output)