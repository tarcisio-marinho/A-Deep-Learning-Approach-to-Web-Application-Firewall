from config import config
from utils import *

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
    dataset = create_dataset(config.get('dataset_path'))
    print('Dataset Size:', len(dataset))
    
    with open('models/dataset3.txt', 'w') as f:
        for i in dataset:
            f.write(i)
            