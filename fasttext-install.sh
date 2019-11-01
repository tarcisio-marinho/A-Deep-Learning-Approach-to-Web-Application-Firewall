#!/bin/bash 

wget https://github.com/facebookresearch/fastText/archive/v0.2.0.zip
unzip v0.2.0.zip
cd fastText-0.2.0
make
sudo cp fasttext /usr/bin